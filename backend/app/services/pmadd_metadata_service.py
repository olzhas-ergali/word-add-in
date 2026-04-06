from __future__ import annotations

from pathlib import Path
from threading import Lock
from typing import Dict, List, Optional


class PmAddMetadataService:
    """
    Extract metadata from 1C calls:
    ПМДобавить("name", valueExpr, "display", Ложь/Истина)
    """

    def __init__(self) -> None:
        # .../backend/app/services/this_file.py -> parents[2] == backend package root (works in repo and in Docker /app)
        backend_root = Path(__file__).resolve().parents[2]
        bundled = backend_root / "1c_pm_sources"
        self._sources = [
            bundled / "ДКП.txt",
            bundled / "ПМСформироватьФормированиеПД.txt",
            bundled / "УСО.txt",
        ]
        self._lock = Lock()
        self._loaded = False
        self._by_name: Dict[str, Dict[str, object]] = {}

    def get_by_name(self) -> Dict[str, Dict[str, object]]:
        if not self._loaded:
            with self._lock:
                if not self._loaded:
                    self._load()
                    self._loaded = True
        return self._by_name

    def _load(self) -> None:
        parsed: Dict[str, Dict[str, object]] = {}
        for source in self._sources:
            if not source.exists():
                continue
            content = source.read_text(encoding="utf-8", errors="ignore")
            for entry in self._extract_calls(content, source.name):
                name = entry["name"]
                current = parsed.get(name)
                if current is None:
                    parsed[name] = entry
                    continue

                # Keep the richer record when duplicates are found.
                if not current.get("display_name") and entry.get("display_name"):
                    current["display_name"] = entry["display_name"]
                if current.get("required") is True and entry.get("required") is False:
                    current["required"] = False
                if not current.get("source_file"):
                    current["source_file"] = entry.get("source_file")

        self._by_name = parsed

    def _extract_calls(self, text: str, source_file: str) -> List[Dict[str, object]]:
        results: List[Dict[str, object]] = []
        needle = "ПМДобавить("
        start = 0
        while True:
            pos = text.find(needle, start)
            if pos == -1:
                break
            args_text, end_pos = self._extract_parenthesized(text, pos + len("ПМДобавить"))
            start = end_pos + 1
            if args_text is None:
                continue

            args = self._split_args(args_text)
            if len(args) < 1:
                continue

            name = self._unquote(args[0])
            if not name:
                continue

            display_name: Optional[str] = None
            if len(args) >= 3:
                display_name = self._unquote(args[2])

            required = True
            if len(args) >= 4:
                required = self._parse_required(args[3], default=True)

            results.append(
                {
                    "name": name,
                    "display_name": display_name,
                    "required": required,
                    "source_file": source_file,
                }
            )
        return results

    def _extract_parenthesized(self, text: str, open_paren_pos: int) -> tuple[Optional[str], int]:
        if open_paren_pos >= len(text) or text[open_paren_pos] != "(":
            return None, open_paren_pos

        depth = 0
        in_string = False
        i = open_paren_pos
        while i < len(text):
            ch = text[i]
            if ch == '"' and (i == 0 or text[i - 1] != "\\"):
                in_string = not in_string
            elif not in_string:
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0:
                        return text[open_paren_pos + 1 : i], i
            i += 1
        return None, i

    def _split_args(self, args_text: str) -> List[str]:
        args: List[str] = []
        buff: List[str] = []
        depth = 0
        in_string = False

        i = 0
        while i < len(args_text):
            ch = args_text[i]
            if ch == '"' and (i == 0 or args_text[i - 1] != "\\"):
                in_string = not in_string
                buff.append(ch)
            elif not in_string and ch in "([{":
                depth += 1
                buff.append(ch)
            elif not in_string and ch in ")]}":
                depth -= 1
                buff.append(ch)
            elif not in_string and depth == 0 and ch == ",":
                args.append("".join(buff).strip())
                buff = []
            else:
                buff.append(ch)
            i += 1

        if buff:
            args.append("".join(buff).strip())
        return args

    def _unquote(self, value: str) -> Optional[str]:
        value = value.strip()
        if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
            return value[1:-1]
        return None

    def _parse_required(self, value: str, default: bool = True) -> bool:
        lowered = value.strip().lower()
        if "ложь" in lowered:
            return False
        if "истина" in lowered:
            return True
        return default


pmadd_metadata_service = PmAddMetadataService()

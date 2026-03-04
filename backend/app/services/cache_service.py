from cachetools import TTLCache
from typing import Optional, Any
from app.config import settings
from app.models.keycloak import KeyCloakToken


class CacheService:

    def __init__(self, maxsize: int = 100, ttl: int = None):
        self.ttl = ttl or settings.cache_ttl
        self._cache = TTLCache(maxsize=maxsize, ttl=self.ttl)

    def cache_token(self, session_id: str, token: KeyCloakToken) -> None:
        self._cache[f"token:{session_id}"] = token

    def get_token(self, session_id: str) -> Optional[KeyCloakToken]:
        return self._cache.get(f"token:{session_id}")

    def remove_token(self, session_id: str) -> None:
        key = f"token:{session_id}"
        if key in self._cache:
            del self._cache[key]

    def set(self, key: str, value: Any) -> None:
        self._cache[key] = value

    def get(self, key: str) -> Optional[Any]:
        return self._cache.get(key)

    def delete(self, key: str) -> None:
        if key in self._cache:
            del self._cache[key]

    def clear(self) -> None:
        self._cache.clear()


cache_service = CacheService()

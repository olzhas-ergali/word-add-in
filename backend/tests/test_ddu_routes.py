import pytest
from pathlib import Path

DDU_PATH = Path(__file__).parent.parent / "variables_export" / "ddu_variables.json"


@pytest.mark.skipif(not DDU_PATH.exists(), reason="ddu_variables.json не найден")
def test_get_ddu_variables(client):
    response = client.get("/api/ddu/variables")
    assert response.status_code == 200
    data = response.json()
    assert "document_id" in data
    assert "variables" in data
    assert isinstance(data["variables"], list)

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.constants import ENCODING_UTF8, ENCODING_UTF8_SIG, DEFAULT_TEXT_ENCODING


@pytest.fixture
def client():
    return TestClient(app)


class TestHealthEndpoints:

    def test_root_returns_ok(self, client: TestClient):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "message" in data
        assert "version" in data

    def test_health_returns_healthy(self, client: TestClient):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "api_version" in data
        assert "keycloak_configured" in data
        assert "printable_forms_configured" in data


class TestEncodingConstants:

    def test_encoding_utf8_is_utf8(self):
        assert ENCODING_UTF8 == "utf-8"

    def test_encoding_utf8_sig_has_bom(self):
        assert ENCODING_UTF8_SIG == "utf-8-sig"

    def test_default_encoding_is_utf8(self):
        assert DEFAULT_TEXT_ENCODING == ENCODING_UTF8

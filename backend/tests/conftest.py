import os
os.environ.setdefault("USE_DATABASE_DIRECT", "false")

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)

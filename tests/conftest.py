import pytest

from app import app


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    _client = app.test_client()
    return _client

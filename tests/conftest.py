import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import database_exists, create_database
from testcontainers.postgres import PostgresContainer

from app import app


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    _client = app.test_client()
    return _client


@pytest.fixture(scope="session")
def db_engine() -> Engine:
    postgres = PostgresContainer("postgres:14.2")
    postgres.start()
    url = postgres.get_connection_url()
    if not database_exists(url):
        create_database(url)
    db_engine = create_engine(url)
    return db_engine

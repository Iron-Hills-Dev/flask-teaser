import logging

from flask import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import database_exists, create_database

from infrastructure.postgres.model.car_entity import CarEntity


def get_db_engine(_db_system: str, _config: Config) -> Engine:
    logging.debug("Creating database engine")
    _url = f"{_db_system}://{_config['TEASER_DB_USER']}:{_config['TEASER_DB_PASS']}@{_config['TEASER_DB_HOST']}:{_config['TEASER_DB_PORT']}/{_config['TEASER_DB_NAME']}"
    if not database_exists(_url):
        logging.warning(f"Database {_config['TEASER_DB_NAME']} don't exists: creating new one")
        create_database(_url)

    engine = create_engine(_url)
    return engine


def init_car_database(_config: Config) -> Engine:
    logging.debug("Initializing database")
    logging.debug("Initializing database engine")
    engine = get_db_engine("postgres", _config)
    logging.debug("Creating/updating database structure")
    car_table = CarEntity()
    car_table.create(engine)
    return engine

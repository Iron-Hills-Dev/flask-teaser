import logging

from flask import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
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


def init_database(_config: Config) -> Engine:
    try:
        logging.debug("Initializing database")
        engine = get_db_engine("postgresql", _config)
        logging.debug("Creating database structure")
        create_car_db_structure(engine)
        logging.debug("Created database structure")
        return engine
    except OperationalError:
        logging.critical("ABORTING INIT - wrong credentials to database")
        exit(1)
    except KeyError as _exc:
        logging.critical(f"ABORTING INIT - missing {_exc.args[0]} environment variable")
        exit(1)


def create_car_db_structure(engine):
    logging.debug("Creating car table")
    car_table = CarEntity()
    car_table.create(engine)
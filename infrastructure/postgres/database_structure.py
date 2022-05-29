import logging

from flask import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

from infrastructure.postgres.model.car_entity import CarEntity
from infrastructure.postgres.model.version_entity import VersionEntity

_STRUCTURE_VERSION_ = 1.0


def init_database(_config: Config) -> Engine:
    try:
        logging.debug("Initializing database")
        engine = get_db_engine("postgresql", _config)
        init_db_structure(engine)
        return engine
    except OperationalError:
        logging.critical("ABORTING INIT - wrong credentials to database")
        exit(1)
    except KeyError as _exc:
        logging.critical(f"ABORTING INIT - missing {_exc.args[0]} environment variable")
        exit(1)


def get_db_engine(_db_system: str, _config: Config) -> Engine:
    logging.debug("Creating database engine")
    _url = f"{_db_system}://{_config['TEASER_DB_USER']}:{_config['TEASER_DB_PASS']}@{_config['TEASER_DB_HOST']}:{_config['TEASER_DB_PORT']}/{_config['TEASER_DB_NAME']}"
    if not database_exists(_url):
        logging.warning(f"Database {_config['TEASER_DB_NAME']} don't exists: creating new one")
        create_database(_url)

    engine = create_engine(_url)
    return engine


def init_db_structure(engine: Engine):
    logging.debug("Checking if database structure exists")
    with Session(engine) as session:
        try:
            _version = session.query(VersionEntity)
            if _version[0].version >= _STRUCTURE_VERSION_:
                logging.warning("Structure already exist - skipping...")
                return None
            elif _version[0].version < _STRUCTURE_VERSION_:
                logging.warning("Structure is outdated - updating...")
                update_db_structure(engine)
        except ProgrammingError as _exc:
            if _exc.code == "f405":
                logging.warning("Structure does not exist - creating...")
                create_db_structure(engine)
            else:
                raise _exc


def create_db_structure(engine):
    logging.debug("Creating database structure")
    create_car_db_structure(engine)
    create_version_reference(engine)
    logging.debug("Created database structure")


def update_db_structure(engine):
    logging.debug("Updating database structure")
    create_db_structure(engine)
    update_version_reference(engine)
    logging.debug("Updated database structure")


def create_version_reference(engine):
    logging.debug("Creating version reference")
    version_table = VersionEntity(version=_STRUCTURE_VERSION_)
    version_table.create(engine)
    with Session(engine) as session:
        session.add(version_table)
        session.commit()


def update_version_reference(engine):
    logging.debug("Updating version reference")
    version_table = VersionEntity(version=_STRUCTURE_VERSION_)
    with Session(engine) as session:
        session.query(VersionEntity).delete()
        session.add(version_table)
        session.commit()


def create_car_db_structure(engine):
    logging.debug("Creating/updating car table")
    car_table = CarEntity()
    car_table.create(engine)

import logging
import shutil
from functools import wraps

from infrastructure.postgres.database_structure import create_car_db_structure
from sqlalchemy.orm import Session

from infrastructure.data_structure.car_file_structure import init_data_structure
from infrastructure.postgres.model.car_entity import CarEntity


def using_car_file_env(_path):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            shutil.rmtree(_path, ignore_errors=True)
            logging.debug("Deleted old data_structure structure")
            logging.debug("Creating new data_structure structure")
            init_data_structure(_path)
            f(*args, **kwargs)

        return wrapper

    return decorator


def using_database(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logging.debug("Creating database structure")
        engine = kwargs["db_engine"]
        create_car_db_structure(engine)
        logging.debug("Created database structure: starting test")

        f(*args, **kwargs)

        logging.debug("Clearing database")
        with Session(engine) as session:
            session.query(CarEntity).delete()
            session.commit()

    return wrapper

import contextlib
import logging
import shutil
from functools import wraps

from sqlalchemy import MetaData

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


def using_car_database(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logging.debug("Creating database structure")
        engine = kwargs["db_engine"]
        cars_table = CarEntity()
        cars_table.create(engine)
        logging.debug("Created database structure: starting test")
        f(*args, **kwargs)
        logging.debug("Clearing database")
        meta = MetaData()
        with contextlib.closing(engine.connect()) as con:
            trans = con.begin()
            for table in reversed(meta.sorted_tables):
                logging.debug(f"Deleting table: {table}")
                con.execute(table.delete())
            trans.commit()

    return wrapper


import logging
import shutil
from functools import wraps

from infrastructure.car_file_module.create_data_structure import init_data_structure


def using_car_file_env(_path):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            shutil.rmtree(_path, ignore_errors=True)
            logging.debug("Deleted old data structure")
            logging.debug("Creating new data structure")
            init_data_structure(_path)
            f(*args, **kwargs)

        return wrapper

    return decorator

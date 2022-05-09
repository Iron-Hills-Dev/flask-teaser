import logging
import os
from os import path

DATA_STRUCTURE_VERSION = "1"


def init_data_structure(_path: str):
    logging.debug(f"Init data_structure structure for car-file-module in {_path}")
    try:
        return create_data_structure(_path)
    except OSError:
        if is_valid_data_folder(_path):
            logging.warning("Data structure already exists - creating aborted")
        else:
            logging.critical("ABORTING INIT - Folder with car data_structure is not empty or it is outdated")
            exit(1)


def is_valid_data_folder(_path: str) -> bool:
    logging.debug("Checking if data_structure folder is valid")
    _real_path = path.join(_path, ".car_file_data_structure")
    if path.exists(_real_path):
        logging.debug("Folder given is valid data_structure folder - checking version")
        with open(_real_path, "r") as _f:
            if _f.read() == DATA_STRUCTURE_VERSION:
                logging.debug("Data folder is up-to-date - returning True")
                return True
            else:
                logging.warning("Data folder is outdated - returning False")
                return False
    else:
        logging.warning("Folder chosen is full and it is not a data_structure folder - returning False")
        return False


def create_data_structure(_path: str) -> bool:
    os.makedirs(_path)
    logging.debug(f"Creating new data_structure structure for car-file-module in {_path}")
    with open(path.join(_path, ".car_file_data_structure"), "w") as _f:
        _f.write(DATA_STRUCTURE_VERSION)
    logging.debug("Created version file")
    os.mkdir(path.join(_path, "cars"))
    logging.debug("Created cars folder for storing cars")
    logging.debug("Created data_structure structure")
    return True

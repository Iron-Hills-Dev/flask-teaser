import logging

from flask import Config

from domain.car.adapter.dummy.dummy_car_modify_adapter import DummyCarModifyAdapter
from domain.car.adapter.dummy.dummy_car_query_adapter import DummyCarQueryAdapter
from domain.car.adapter.file.file_car_modify_adapter import FileCarModifyAdapter
from domain.car.adapter.file.file_car_query_adapter import FileCarQueryAdapter
from domain.car.adapter.in_memory.in_memory_car_modify_adapter import InMemoryCarModifyAdapter
from domain.car.adapter.in_memory.in_memory_car_query_adapter import InMemoryCarQueryAdapter
from domain.car.car_modify_port import CarModifyPort
from domain.car.car_query_port import CarQueryPort
from infrastructure.data_structure.car_file_structure import init_data_structure


# This is global application ports configuration

class AppPorts:
    def __init__(self, _config: Config) -> None:
        self.car_modify_port, self.car_query_port = config_car_module(_config)


def config_car_module(_config: Config) -> [CarModifyPort, CarQueryPort]:
    """
    Prepares configuration of ports in CAR module
    """
    logging.info("Configuring car ports")
    match _config.get('TEASER_CAR_PORT'):
        case "DUMMY":
            logging.info("Configuring DUMMY car ports")
            return DummyCarModifyAdapter(), DummyCarQueryAdapter()
        case "IN_MEMORY":
            logging.info("Configuring IN MEMORY car ports")
            return InMemoryCarModifyAdapter(), InMemoryCarQueryAdapter()
        case "FILE":
            logging.info("Configuring FILE car ports")
            init_data_structure(_config.get("TEASER_CAR_DATA_DIR"))
            return FileCarModifyAdapter(_config.get('TEASER_CAR_DATA_DIR')), FileCarQueryAdapter(
                _config.get('TEASER_CAR_DATA_DIR'))
        case _:
            logging.critical("ABORTING INIT - unknown TEASER_CAR_PORT environment variable")
            exit(1)

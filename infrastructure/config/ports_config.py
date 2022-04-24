import logging

from flask import Config

from domain.car.adapter.dummy.dummy_car_modify_port import DummyCarModifyPort
from domain.car.adapter.dummy.dummy_car_query_port import DummyCarQueryPort
from domain.car.adapter.in_memory.in_memory_car_modify_port import InMemoryCarModifyPort
from domain.car.adapter.in_memory.in_memory_car_query_port import InMemoryCarQueryPort
from domain.car.car_modify_port import CarModifyPort
from domain.car.car_query_port import CarQueryPort


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
            return DummyCarModifyPort(), DummyCarQueryPort()
        case "IN_MEMORY":
            logging.info("Configuring IN MEMORY car ports")
            return InMemoryCarModifyPort(), InMemoryCarQueryPort()
        case _:
            logging.critical("ABORTING INIT - unknown TEASER_CAR_PORT environment variable")
            exit(1)

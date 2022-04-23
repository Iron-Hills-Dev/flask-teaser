import logging
from os import environ

from domain.car.car_modify_port import CarModifyPort
from domain.car.car_query_port import CarQueryPort
from domain.car.adapter.dummy.dummy_car_modify_port import DummyCarModifyPort
from domain.car.adapter.dummy.dummy_car_query_port import DummyCarQueryPort
from domain.car.adapter.in_memory.in_memory_car_modify_port import InMemoryCarModifyPort
from domain.car.adapter.in_memory.in_memory_car_query_port import InMemoryCarQueryPort


# This is global application ports configuration

class AppPorts:
    def __init__(self, _app) -> None:
        self.car_modify_port, self.car_query_port = config_car_module(_app)


def config_car_module(_app) -> [CarModifyPort, CarQueryPort]:
    """
    Prepares configuration of ports in CAR module
    """
    logging.info("Configuring car ports")

    if environ.get("CAR_PORT") is None:
        logging.critical("ABORTING INIT - CAR_PORT environment variable not given")
        exit(1)
    else:
        _app.config.update({"CAR_PORT": environ.get("CAR_PORT")})
        logging.debug("Variable CAR_PORT has been saved in app config")

    if _app.config["CAR_PORT"] == "DUMMY":
        # DUMMY configuration
        logging.info("Configuring DUMMY car ports")
        return DummyCarModifyPort(), DummyCarQueryPort()
    elif _app.config["CAR_PORT"] == "IN_MEMORY":
        # IN MEMORY configuration
        logging.info("Configuring IN MEMORY car ports")
        return InMemoryCarModifyPort(), InMemoryCarQueryPort()
    else:
        logging.critical("ABORTING INIT - CAR_PORT environment variable is not valid with any existing car port")
        exit(1)

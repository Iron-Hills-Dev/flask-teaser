import logging

from domain.car.CarModifyPort import CarModifyPort
from domain.car.CarQueryPort import CarQueryPort
from domain.car.adapter.dummy.DummyCarModifyPort import DummyCarModifyPort
from domain.car.adapter.dummy.DummyCarQueryPort import DummyCarQueryPort
from domain.car.adapter.in_memory.in_memory_car_modify_port import InMemoryCarModifyPort
from domain.car.adapter.in_memory.in_memory_car_query_port import InMemoryCarQueryPort


# This is global application ports configuration

class AppPorts:
    def __init__(self, _port: str) -> None:
        self.car_modify_port, self.car_query_port = config_car_module(_port)


def config_car_module(_port) -> [CarModifyPort, CarQueryPort]:
    """
    Prepares configuration of ports in CAR module
    """
    if _port == "DUMMY":
        # DUMMY configuration
        logging.info("Configuring DUMMY Car Ports")
        return DummyCarModifyPort(), DummyCarQueryPort()
    elif _port == "IN_MEMORY":
        # IN MEMORY configuration
        logging.info("[config_car_module] Configuring IN MEMORY car ports")
        return InMemoryCarModifyPort(), InMemoryCarQueryPort()
    else:
        raise ModuleNotFoundError

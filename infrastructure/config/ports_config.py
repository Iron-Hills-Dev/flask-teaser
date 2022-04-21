import logging

from domain.car.CarModifyPort import CarModifyPort
from domain.car.CarQueryPort import CarQueryPort
from domain.car.adapter.dummy.DummyCarModifyPort import DummyCarModifyPort
from domain.car.adapter.dummy.DummyCarQueryPort import DummyCarQueryPort


# This is global application ports configuration
class AppPorts:

    def __init__(self) -> None:
        self.car_modify_port, self.car_query_port = config_car_module()


def config_car_module() -> [CarModifyPort, CarQueryPort]:
    """
    Prepares configuration of ports in CAR module
    """
    # for now only Dummy implementation
    logging.info("Configuring DUMMY Car Ports")
    return DummyCarModifyPort(), DummyCarQueryPort()

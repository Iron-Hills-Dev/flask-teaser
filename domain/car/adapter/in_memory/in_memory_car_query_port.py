import logging
import uuid

from data.car_dict_in_memory import cars
from domain.car.CarQueryPort import CarQueryPort
from domain.car.model.Car import Car


class InMemoryCarQueryPort(CarQueryPort):
    def find_car(self, _uuid: uuid.UUID) -> Car:
        logging.debug("[find_car] Function triggered")
        _car = cars[str(_uuid)]
        logging.debug(f"[find_car] Found car {str(_uuid)} in memory")
        return _car

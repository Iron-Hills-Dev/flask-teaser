import logging
import uuid

from domain.car.adapter.in_memory.car_dict import cars
from domain.car.car_query_port import CarQueryPort
from domain.car.model.car import Car


class InMemoryCarQueryAdapter(CarQueryPort):
    def find_car(self, _car_id: uuid.UUID) -> Car:
        logging.debug(f"Trying to find car with ID: {_car_id}")
        _car = cars[str(_car_id)]
        logging.debug(f"Successfully found chosen car: {_car}")
        return _car

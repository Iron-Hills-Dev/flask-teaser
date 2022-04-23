import logging
import uuid

from domain.car.car_query_port import CarQueryPort
from domain.car.model.car import Car


class DummyCarQueryPort(CarQueryPort):

    def find_car(self, _car_id: uuid.UUID) -> Car:
        fake_car = Car(_car_id, "Porsche Cayenne", "XX 1234")
        logging.debug(f"Found fake car (always same data): {fake_car}")
        return fake_car

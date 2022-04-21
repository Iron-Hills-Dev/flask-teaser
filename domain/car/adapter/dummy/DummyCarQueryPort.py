import logging
import uuid

from domain.car.CarQueryPort import CarQueryPort
from domain.car.model.Car import Car


class DummyCarQueryPort(CarQueryPort):

    def find_car(self, _id: uuid) -> Car:
        fake_car = Car(_id, "Porsche Cayenne", "XX 1234")
        logging.debug(f"Found fake car (always same data): {fake_car}")
        return fake_car

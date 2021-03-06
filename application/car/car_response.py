import json

from domain.car.model.car import Car


class CarResponse:
    def __init__(self, _car: Car) -> None:
        self.id = str(_car.id)
        self.model = _car.model
        self.regNum = _car.registration_number

    def to_json(self):
        return self.__dict__

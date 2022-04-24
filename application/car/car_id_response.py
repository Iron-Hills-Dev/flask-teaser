import json
import uuid

from domain.car.model.car import Car


class CarIdResponse:
    def __init__(self, _car_id: uuid) -> None:
        self.id = str(_car_id)

    def to_json(self):
        return self.__dict__

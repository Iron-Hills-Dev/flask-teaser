import json
import uuid

from domain.car.model.Car import Car


class CarIdResponse:
    def __init__(self, _id: uuid) -> None:
        self.id = str(_id)

    def to_json(self):
        return json.dumps(self.__dict__)

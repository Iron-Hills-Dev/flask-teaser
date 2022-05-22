import json
import logging
from os import path
from types import SimpleNamespace
from uuid import UUID

from domain.car.car_query_port import CarQueryPort
from domain.car.model.car import Car


class FileCarQueryAdapter(CarQueryPort):
    def __init__(self, _data_path: str) -> None:
        self.data_path = _data_path
        super().__init__()

    def find_car(self, _car_id: UUID) -> Car:
        logging.debug(f"Searching for car: {_car_id}")
        _path = path.join(self.data_path, f"cars/{_car_id}.json")
        if path.exists(_path):
            logging.debug("Car file found - will read it")
            _str_json = None
            with open(_path, "r") as _f:
                _str_json = str(_f.read())
            _car = json.loads(_str_json, object_hook=lambda car: SimpleNamespace(**car))
            _car = Car(_car.car_id, _car.model, _car.registration_number)
            logging.debug(f"Successfully read car: {_car.to_dict()}")
            return _car
        else:
            logging.error("Car with such ID does not exists")
            raise FileNotFoundError

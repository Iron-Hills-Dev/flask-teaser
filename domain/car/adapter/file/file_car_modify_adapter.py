import json
import logging
import os
from os import path
from uuid import UUID, uuid1

from domain.car.car_modify_port import CarModifyPort
from domain.car.model.car import Car
from domain.car.model.car_add_command import CarAddCommand


class FileCarModifyAdapter(CarModifyPort):
    def __init__(self, _data_path: str) -> None:
        self.data_path = _data_path

    def add_car(self, _cmd: CarAddCommand) -> UUID:
        logging.debug(f"Adding car: {_cmd}")
        _car = Car(car_id=uuid1(), model=_cmd.model, registration_number=_cmd.registration_number)
        _json = _car.to_dict()
        _json["id"] = str(_json["id"])
        with open(path.join(self.data_path, f"cars/{_car.id}.json"), "w") as _f:
            json.dump(_json, _f, ensure_ascii=False, indent=4)
        logging.debug(f"Car successfully added: id: {_car.id}")
        return _car.id

    def delete_car(self, _car_id: UUID) -> None:
        logging.debug(f"Removing car with id {_car_id}")
        _path = path.join(self.data_path, f"cars/{_car_id}.json")
        if path.exists(_path):
            logging.debug("Car with this id has been found - removing")
            os.remove(_path)
            logging.debug("Removed car successfully")
        else:
            logging.error("Car with given ID does not exist")
            raise FileNotFoundError

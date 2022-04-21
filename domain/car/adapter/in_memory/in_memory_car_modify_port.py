import logging
import uuid

from data.car_dict_in_memory import cars
from domain.car.CarModifyPort import CarModifyPort
from domain.car.model.Car import Car
from domain.car.model.CarAddCommand import CarAddCommand


class InMemoryCarModifyPort(CarModifyPort):
    def add_car(self, _cmd: CarAddCommand) -> uuid.UUID:
        logging.debug("[add_car] Triggered function")
        _car = Car(uuid=uuid.uuid1(), model=_cmd.model, registration_number=_cmd.registration_number)
        cars.setdefault(str(_car.uuid), _car)
        logging.debug(f"[add_car] Saved car {str(_car.uuid)} to global in memory dict")
        return _car.uuid

    def delete_car(self, _uuid: uuid.UUID) -> bool:
        logging.debug("[remove_car] Triggered function")
        cars.pop(_uuid)
        logging.debug(f"[remove_car] Successfully removed car {str(_uuid)}")
        return True

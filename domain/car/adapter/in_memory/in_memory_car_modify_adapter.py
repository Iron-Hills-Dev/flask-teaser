import logging
import uuid

from domain.car.adapter.in_memory.car_dict import cars
from domain.car.car_modify_port import CarModifyPort
from domain.car.model.car import Car
from domain.car.model.car_add_command import CarAddCommand


class InMemoryCarModifyAdapter(CarModifyPort):
    def add_car(self, _cmd: CarAddCommand) -> uuid.UUID:
        logging.debug(f"Adding car: {_cmd}")
        _car = Car(car_id=uuid.uuid1(), model=_cmd.model, registration_number=_cmd.registration_number)
        cars.setdefault(str(_car.id), _car)
        logging.debug(f"Saved car using ID: {str(_car.id)}")
        return _car.id

    def delete_car(self, _car_id: uuid.UUID) -> None:
        logging.debug(f"Removing car with ID: {_car_id}")
        cars.pop(str(_car_id))
        logging.debug(f"Successfully removed chosen car")

import logging
import uuid

from domain.car.CarModifyPort import CarModifyPort
from domain.car.model.CarAddCommand import CarAddCommand


class DummyCarModifyPort(CarModifyPort):
    def add_car(self, _cmd: CarAddCommand) -> uuid:
        logging.debug(f'processing command: {_cmd}')
        car_id = uuid.uuid4()
        logging.debug(f'Generated random car_id: {car_id}')
        return car_id

    def delete_car(self, _id: uuid) -> None:
        logging.debug(f"Deleting car (it's a fake): car_id={_id}")
        pass

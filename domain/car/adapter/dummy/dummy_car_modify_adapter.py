import logging
import uuid

from domain.car.car_modify_port import CarModifyPort
from domain.car.model.car_add_command import CarAddCommand


class DummyCarModifyAdapter(CarModifyPort):
    def add_car(self, _cmd: CarAddCommand) -> uuid:
        logging.debug(f'processing command: {_cmd}')
        car_id = uuid.uuid4()
        logging.debug(f'Generated random car_id: {car_id}')
        return car_id

    def delete_car(self, _car_id: uuid.UUID) -> None:
        logging.debug(f"Deleting car (it's a fake): car_id={_car_id}")

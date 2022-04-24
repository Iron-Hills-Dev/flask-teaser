import abc
import uuid
from abc import ABC

from domain.car.model.car_add_command import CarAddCommand


class CarModifyPort(ABC):

    @abc.abstractmethod
    def add_car(self, _cmd: CarAddCommand) -> uuid:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_car(self, _car_id: uuid) -> None:
        raise NotImplementedError

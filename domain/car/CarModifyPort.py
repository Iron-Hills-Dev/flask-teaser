import abc
import uuid
from abc import ABC

from domain.car.model.CarAddCommand import CarAddCommand


class CarModifyPort(ABC):

    @abc.abstractmethod
    def add_car(self, _cmd: CarAddCommand) -> uuid:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_car(self, _id: uuid) -> None:
        raise NotImplementedError

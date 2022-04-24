import abc
from abc import ABC
from uuid import UUID

from domain.car.model.car_add_command import CarAddCommand


class CarModifyPort(ABC):

    @abc.abstractmethod
    def add_car(self, _cmd: CarAddCommand) -> UUID:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_car(self, _car_id: UUID) -> bool:
        raise NotImplementedError

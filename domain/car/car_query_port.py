import abc
from abc import ABC
from uuid import UUID

from domain.car.model.car import Car


class CarQueryPort(ABC):

    @abc.abstractmethod
    def find_car(self, _car_id: UUID) -> Car:
        raise NotImplementedError

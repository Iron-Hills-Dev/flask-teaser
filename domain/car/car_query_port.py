import abc
import uuid
from abc import ABC

from domain.car.model.car import Car


class CarQueryPort(ABC):

    @abc.abstractmethod
    def find_car(self, _car_id: uuid) -> Car:
        raise NotImplementedError

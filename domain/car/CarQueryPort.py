import abc
import uuid
from abc import ABC

from domain.car.model.Car import Car


class CarQueryPort(ABC):

    @abc.abstractmethod
    def find_car(self, _id: uuid) -> Car:
        raise NotImplementedError

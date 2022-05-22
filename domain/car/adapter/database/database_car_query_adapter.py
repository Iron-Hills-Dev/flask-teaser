import logging
import uuid

from sqlalchemy.orm import sessionmaker

from domain.car.car_query_port import CarQueryPort
from domain.car.model.car import Car
from infrastructure.postgres.model.car_entity import CarEntity


class DatabaseCarQueryAdapter(CarQueryPort):
    def __init__(self, db_engine):
        self.engine = db_engine

    def find_car(self, _car_id: uuid.UUID) -> Car:
        with sessionmaker(bind=self.engine)() as session:
            logging.debug(f"Searching for car {_car_id}")
            _car = session.query(CarEntity).filter(CarEntity.car_id == _car_id).first()
            _car = Car(car_id=_car.car_id, model=_car.model, registration_number=_car.registration_number)
            logging.debug(f"Successfully found car: {_car.to_dict()}")
            return _car

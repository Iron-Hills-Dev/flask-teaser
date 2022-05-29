import logging
from uuid import UUID, uuid4

from sqlalchemy.orm import sessionmaker

from domain.car.car_modify_port import CarModifyPort
from domain.car.model.car import Car
from domain.car.model.car_add_command import CarAddCommand
from infrastructure.postgres.model.car_entity import CarEntity


class DatabaseCarModifyAdapter(CarModifyPort):
    def __init__(self, db_engine):
        self.engine = db_engine

    def add_car(self, _cmd: CarAddCommand) -> UUID:
        logging.debug(f'Adding car: {_cmd}')
        _car = Car(car_id=uuid4(), model=_cmd.model, registration_number=_cmd.registration_number)
        with sessionmaker(bind=self.engine)() as session:
            _db_car = CarEntity(car_id=_car.id, model=_car.model, registration_number=_car.registration_number)
            session.add(_db_car)
            session.commit()
        return _car.id

    def delete_car(self, _car_id: UUID) -> None:
        logging.debug(f"Deleting car: {_car_id}")
        with sessionmaker(bind=self.engine)() as session:
            _car = session.query(CarEntity).filter(CarEntity.car_id == _car_id).first()
            logging.debug("Car exists: proceed to delete")
            session.delete(_car)
            session.commit()
        logging.debug("Successfully deleted car")

import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

_base_ = declarative_base()


class CarEntity(_base_):
    __tablename__ = "car"
    car_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    model = Column(String(150))
    registration_number = Column(String(15))

    def create(self, engine):
        _base_.metadata.create_all(engine)

    def to_dict(self):
        return self.__dict__

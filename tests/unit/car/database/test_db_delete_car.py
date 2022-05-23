import logging
import uuid

import pytest
from sqlalchemy.orm.exc import UnmappedInstanceError

from domain.car.adapter.database.database_car_modify_adapter import DatabaseCarModifyAdapter
from domain.car.adapter.database.database_car_query_adapter import DatabaseCarQueryAdapter
from domain.car.model.car_add_command import CarAddCommand
from tests.decors import using_car_database


@using_car_database
def test_should_delete(db_engine):
    car_modify, car_query = DatabaseCarModifyAdapter(db_engine), DatabaseCarQueryAdapter(db_engine)
    # given
    _cmd = CarAddCommand(model="Lamborghini Hurracan", registration_number="EPA1234")
    _uuid = car_modify.add_car(_cmd)

    # when & then
    with pytest.raises(AttributeError) as _exc:
        car_modify.delete_car(_uuid)
        car_query.find_car(_uuid)


@using_car_database
def test_should_not_delete_fake_car(db_engine):
    car_modify, car_query = DatabaseCarModifyAdapter(db_engine), DatabaseCarQueryAdapter(db_engine)
    # given
    _fake_uuid = uuid.uuid1()

    # when & then
    with pytest.raises(UnmappedInstanceError) as _exc:
        car_modify.delete_car(_fake_uuid)

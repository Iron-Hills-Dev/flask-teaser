import logging
import uuid

from app import app
from domain.car.adapter.file.file_car_modify_port import FileCarModifyPort
from domain.car.adapter.file.file_car_query_port import FileCarQueryPort
from domain.car.model.car_add_command import CarAddCommand
from tests.decors import using_car_file_env

car_modify, car_query = FileCarModifyPort(app.config["TEASER_CAR_DATA_DIR"]), FileCarQueryPort(
    app.config["TEASER_CAR_DATA_DIR"])


@using_car_file_env(car_modify.data_path)
def test_should_delete():
    # given
    _cmd = CarAddCommand(model="Lamborghini Hurracan", registration_number="EPA1234")
    _uuid = car_modify.add_car(_cmd)

    # when
    try:
        car_modify.delete_car(_uuid)
        car_query.find_car(_uuid)

    # then
    except FileNotFoundError as _exc:
        assert 1 == 1


@using_car_file_env(car_modify.data_path)
def test_should_not_delete_fake_car():
    # given
    _fake_uuid = uuid.uuid1()

    # when
    try:
        car_modify.delete_car(_fake_uuid)

    # then
    except FileNotFoundError as _exc:
        assert 1 == 1

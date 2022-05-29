import uuid

import pytest

from app import app
from domain.car.adapter.file.file_car_modify_adapter import FileCarModifyAdapter
from domain.car.adapter.file.file_car_query_adapter import FileCarQueryAdapter
from domain.car.model.car_add_command import CarAddCommand
from tests.decors import using_car_file_env

car_modify, car_query = FileCarModifyAdapter(app.config["TEASER_CAR_DATA_DIR"]), FileCarQueryAdapter(
    app.config["TEASER_CAR_DATA_DIR"])


@using_car_file_env(car_modify.data_path)
def test_should_delete():
    # given
    _cmd = CarAddCommand(model="Lamborghini Hurracan", registration_number="EPA1234")
    _uuid = car_modify.add_car(_cmd)

    # when
    with pytest.raises(FileNotFoundError) as _exc:
        car_modify.delete_car(_uuid)
        car_query.find_car(_uuid)

        # then
        assert 1 == 1


@using_car_file_env(car_modify.data_path)
def test_should_not_delete_fake_car():
    # given
    _fake_uuid = uuid.uuid1()

    # when
    with pytest.raises(FileNotFoundError) as _exc:
        car_modify.delete_car(_fake_uuid)

        # then
        assert 1 == 1

from app import app
from domain.car.adapter.file.file_car_modify_adapter import FileCarModifyAdapter
from domain.car.adapter.file.file_car_query_adapter import FileCarQueryAdapter
from domain.car.model.car_add_command import CarAddCommand
from tests.decors import using_car_file_env

car_modify, car_query = FileCarModifyAdapter(app.config["TEASER_CAR_DATA_DIR"]), FileCarQueryAdapter(
    app.config["TEASER_CAR_DATA_DIR"])


@using_car_file_env(car_modify.data_path)
def test_should_save_correctly():
    # given
    _cmd = CarAddCommand(model="Lamborghini Hurracan", registration_number="EPA1234")

    # when
    _uuid = car_modify.add_car(_cmd)

    # then
    _car = car_query.find_car(_uuid)
    assert _car.id == _uuid
    assert _car.model == "Lamborghini Hurracan"
    assert _car.registration_number == "EPA1234"

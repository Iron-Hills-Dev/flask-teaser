from domain.car.adapter.database.database_car_modify_adapter import DatabaseCarModifyAdapter
from domain.car.adapter.database.database_car_query_adapter import DatabaseCarQueryAdapter
from domain.car.model.car_add_command import CarAddCommand
from tests.decors import using_database


@using_database
def test_should_save_correctly(db_engine):
    car_modify, car_query = DatabaseCarModifyAdapter(db_engine), DatabaseCarQueryAdapter(db_engine)

    # given
    _cmd = CarAddCommand(model="Lamborghini Hurracan", registration_number="EPA1234")

    # when
    _uuid = car_modify.add_car(_cmd)

    # then
    _car = car_query.find_car(_uuid)
    assert _car.id == _uuid
    assert _car.model == "Lamborghini Hurracan"
    assert _car.registration_number == "EPA1234"

from domain.car.adapter.in_memory.in_memory_car_modify_port import InMemoryCarModifyPort
from domain.car.adapter.in_memory.in_memory_car_query_port import InMemoryCarQueryPort
from domain.car.model.car_add_command import CarAddCommand

car_modify = InMemoryCarModifyPort()
car_query = InMemoryCarQueryPort()


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

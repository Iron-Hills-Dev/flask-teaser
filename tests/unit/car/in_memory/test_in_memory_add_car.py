import uuid

from domain.car.adapter.in_memory.in_memory_car_modify_adapter import InMemoryCarModifyAdapter
from domain.car.adapter.in_memory.in_memory_car_query_adapter import InMemoryCarQueryAdapter
from domain.car.model.car_add_command import CarAddCommand

car_modify, car_query = InMemoryCarModifyAdapter(), InMemoryCarQueryAdapter()


def test_should_save_correctly():
    # given
    _uuid4 = uuid.uuid4()
    _uuid4_str = str(_uuid4)
    _uuid4_reconverted = uuid.UUID(_uuid4_str)
    assert _uuid4 == _uuid4_reconverted

    _cmd = CarAddCommand(model="Lamborghini Hurracan", registration_number="EPA1234")

    # when
    _uuid = car_modify.add_car(_cmd)

    # then
    _car = car_query.find_car(_uuid)
    assert _car.id == _uuid
    assert _car.model == "Lamborghini Hurracan"
    assert _car.registration_number == "EPA1234"

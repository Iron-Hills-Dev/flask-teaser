import uuid

from domain.car.adapter.in_memory.in_memory_car_modify_port import InMemoryCarModifyPort
from domain.car.adapter.in_memory.in_memory_car_query_port import InMemoryCarQueryPort
from domain.car.model.car_add_command import CarAddCommand

car_modify = InMemoryCarModifyPort()
car_query = InMemoryCarQueryPort()


def test_should_delete():
    # given
    _cmd = CarAddCommand(model="Lamborghini Hurracan", registration_number="EPA1234")
    _uuid = car_modify.add_car(_cmd)

    # when
    try:
        car_modify.delete_car(_uuid)
        car_query.find_car(_uuid)

    # then
    except KeyError as _exc:
        assert _exc.args[0] == str(_uuid)


def test_should_not_delete_fake_car():
    # given
    _fake_uuid = uuid.uuid1()

    # when
    try:
        car_modify.delete_car(_fake_uuid)

    # then
    except KeyError as _exc:
        assert _exc.args[0] == str(_fake_uuid)

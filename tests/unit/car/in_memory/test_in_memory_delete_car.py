import uuid

import pytest

from domain.car.adapter.in_memory.in_memory_car_modify_adapter import InMemoryCarModifyAdapter
from domain.car.adapter.in_memory.in_memory_car_query_adapter import InMemoryCarQueryAdapter
from domain.car.model.car_add_command import CarAddCommand

car_modify, car_query = InMemoryCarModifyAdapter(), InMemoryCarQueryAdapter()


def test_should_delete():
    # given
    _cmd = CarAddCommand(model="Lamborghini Hurracan", registration_number="EPA1234")
    _uuid = car_modify.add_car(_cmd)

    # when
    with pytest.raises(KeyError) as _exc:
        car_modify.delete_car(_uuid)
        car_query.find_car(_uuid)

    # then
        assert _exc.value.args[0] == str(_uuid)


def test_should_not_delete_fake_car():
    # given
    _fake_uuid = uuid.uuid1()

    # when
    with pytest.raises(KeyError) as _exc:
        car_modify.delete_car(_fake_uuid)

    # then
        assert _exc.value.args[0] == str(_fake_uuid)

from datetime import date

import pytest

from domain.date import month_service


@pytest.mark.parametrize("_date,_expected", [
    (date(2022, 4, 12), 18),
    (date(2022, 1, 31), 0),
    (date(2022, 2, 1), 27),
    (date(2020, 2, 1), 28),
    (date(2021, 5, 10), 21),

])
def test(_date, _expected):
    # when
    _days_left = month_service.get_days_left(_date)

    # then
    assert _days_left == _expected

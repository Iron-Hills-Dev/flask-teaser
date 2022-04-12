from calendar import monthrange
from datetime import date


def get_days_left(_date: date) -> int:
    """
    Counts amount of days left to the end of the month.
    :return: As above.
    """
    _act_month = _date.month
    _act_year = _date.year
    _act_day = _date.day
    _days_in_month = monthrange(_act_year, _act_month)[1]
    return _days_in_month - _act_day



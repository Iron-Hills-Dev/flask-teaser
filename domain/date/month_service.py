from calendar import monthrange
from datetime import datetime


def get_days_left() -> int:
    """
    Gets actual month, year and day using datetime library. Then using monthrange function from calendar lib it gets
    amount of days in actual month. Returns actual monthday number subtracted from amount of days in month.
    :return: Amount of days left to the end of the month.
    """
    _act_month = datetime.utcnow().month
    _act_year = datetime.utcnow().year
    _act_day = datetime.utcnow().day
    _days_in_month = monthrange(_act_year, _act_month)[1]
    return _days_in_month - _act_day

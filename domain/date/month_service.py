from calendar import monthrange
from datetime import datetime


def get_days_left():
    # TODO docs
    _act_month = datetime.utcnow().month
    _act_year = datetime.utcnow().year
    _act_day = datetime.utcnow().day
    _days_in_month = monthrange(_act_year, _act_month)[1]
    return _days_in_month - _act_day

import logging
from calendar import monthrange
from datetime import date


def get_days_left(_date: date) -> int:
    """
    Counts amount of days left to the end of the month.
    :param _date: Date from which function will calculate days left to month end.
    :return: As above.
    """
    logging.debug(f"[month_service] [get_days_left] Function triggered (date given: {_date}).")
    _month = _date.month
    _year = _date.year
    _day = _date.day
    _days_in_month = monthrange(_year, _month)[1]
    logging.debug(f"[month_service] [get_days_left] Days left in month: {_days_in_month - _day}")
    return _days_in_month - _day



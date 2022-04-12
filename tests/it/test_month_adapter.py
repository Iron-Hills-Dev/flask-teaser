from datetime import date

from app import app
from domain.date import month_service


def test_should_respond_correctly():
    # given
    app.config.update({"TESTING": True})
    client = app.test_client()

    # when
    res = client.get("/month/days-left")

    # then
    assert res.status_code == 200
    assert res.json == {"daysLeft": month_service.get_days_left(date.today())}

from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.relativedelta import SU, MO, TU, WE, TH, FR, SA
from calendar import monthrange


class Weekday(object):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


WEEKDAYS = {
    0: MO,
    1: TU,
    2: WE,
    3: TH,
    4: FR,
    5: SA,
    6: SU
}


def meetup_date(year, month, *, nth=4, weekday=Weekday.THURSDAY):
    if nth == 0:
        raise ValueError
    if nth < 1:
        return date(year, month, monthrange(year, month)[1]) + relativedelta(
            weekday=WEEKDAYS[weekday](nth))
    return date(year, month, 1) + relativedelta(weekday=WEEKDAYS[weekday](nth))

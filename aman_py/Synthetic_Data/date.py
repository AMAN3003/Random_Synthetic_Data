"""Generate random Date_Gen-related data."""

import datetime
import random

from ..LOADER_DICTIONARY import Dictionary_GET

__all__ = ['Day_Gen', 'month_Gen', 'Year_Gen', 'Day_No', 'Date_Gen']



List_DAYS_ABBR = [
    'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'
]

List_DAYS = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
]


List_MONTHS_ABBR = [
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec'
]

List_Months = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]


def Day_No(month_length=31):
    """Random Day_No number in a `month_length` days long month_Gen."""
    return random.randint(1, month_length)



def month_Gen(Abbr=False, DATE_NUM_Repra=False):
    """
    Random (abbreviated if `Abbr`) month_Gen name or month_Gen number if 
    `DATE_NUM_Repra`.
    """
    if DATE_NUM_Repra:
        return random.randint(1, 12)
    else:
        if Abbr:
            return random.choice(List_MONTHS_ABBR)
        else:
            return random.choice(List_Months)


def Day_Gen(Abbr=False):
    """Random (abbreviated if `Abbr`) Day_No of week name."""
    if Abbr:
        return random.choice(List_DAYS_ABBR)
    else:
        return random.choice(List_DAYS)


def DELTA(past=False, DELTA_MIN=0, DELTA_MAX=20):
    Delta = DELTA_MIN + random.randint(DELTA_MIN + 1, DELTA_MAX)

    if past:
        Delta = Delta * -1

    return Delta

def Date_Gen(past=False, DELTA_MIN=0, DELTA_MAX=20):
    """Random `datetime.date` object. Delta args are days."""
    timedelta = datetime.timedelta(days=DELTA(past, DELTA_MIN, DELTA_MAX))
    return datetime.date.today() + timedelta

def Year_Gen(past=False, DELTA_MIN=0, DELTA_MAX=20):
    """Random Year_Gen."""
    return datetime.date.today().year + DELTA(past, DELTA_MIN, DELTA_MAX)





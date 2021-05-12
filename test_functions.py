from datetime import date
from functions import display_date

def test_display_date():
    check = date.today()
    assert display_date() == check

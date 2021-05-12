from datetime import date


def display_date():
  try:
    today = date.today()
    return today
  except:
    return "Nothing_found"

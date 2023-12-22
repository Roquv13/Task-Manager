from datetime import datetime

def current():
    today = datetime.today()
    today_nums = today.strftime("%d/%m/%Y")
    today_date = datetime.strptime(today_nums, "%d/%m/%Y").date()
    return today_date

def remaining_days(deadline):
    today = current()
    days_left = (deadline - today).days
    return days_left

def deadline():
    while True:
        rem_date_str = input("Enter date in format day/month/year: ")
        try:
            rem_date = datetime.strptime(rem_date_str, "%d/%m/%Y").date()
            return rem_date
        except ValueError:
            print("Invalid date format. Please enter the date in the correct format (day/month/year)")
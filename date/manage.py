from datetime import datetime

task_deadlines = {}

def current():
    today = datetime.today()
    today_nums = today.strftime("%d/%m/%Y")
    today_date = datetime.strptime(today_nums, "%d/%m/%Y").date()
    return today_date

def remaining_days(task):
    today = current()
    if task in task_deadlines:
        days_left = (task_deadlines[task] - today).days
        if days_left >= 0:
            return f"remaining days: {days_left}"
        else:
            return f"days after: {abs(days_left)}"
    else:
        return None

def get_deadline(task):
    if task in task_deadlines:
        task_deadline = task_deadlines[task]
        return task_deadline
    else:
        print("Deadline is not setted")

def add_deadline(task, deadline):
    try:
        task_deadlines[task] = deadline
        print(f"Deadline set for task {task}")
    except ValueError:
        print("Invalid date format.")

def set_deadline(task):
    if task in task_deadlines:
        print("Task already has a deadline set.")
        task_deadline = get_deadline(task)
        print(f"Deadline for this task: {task_deadline}")
    else:
        while True:
            rem_date_str = input("Enter date in format day/month/year: ")
            try:
                rem_date = datetime.strptime(rem_date_str, "%d/%m/%Y").date()
                task_deadlines[task] = rem_date
                print(f"Deadline set for task '{task}': {rem_date.strftime('%d/%m/%Y')}")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the correct format (day/month/year)")
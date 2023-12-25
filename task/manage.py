import exceptions
import mark.manage
import date.manage

def get_name():
    name = input("Enter name of task: ")
    return name

def get_text():
    text = input("Enter text for task: ")
    return text

def get_task():
    try:
        name = get_name()
        text = get_text()
        return name, text
    except Exception as e:
        print(f"Error: {e}")

def get_tasks(tasks):
    if len(tasks) == 0:
            print("There is no task.")
    else:
        print("All of created tasks:")
        for name_task, task in tasks.items():
            print(name_task)
    
def add(tasks):
    try:
        name, text = get_task()
        if name in tasks:
            raise exceptions.ExistsException("Task already exists")
        tasks[name] = text
        date.manage.get_deadline(name)
        print(f"Task '{name}' added.")
    except exceptions.ExistsException as e:
        print(f"Error: {e}")

def delete(tasks):
    try:
        name = get_name()
        if name not in tasks:
            raise exceptions.ExistsException("Task does not exists.")
        tasks.pop(name)
    except Exception as e:
        print(f"Error: {e}")

def edit(tasks):
    try:
        name = get_name()
        if name not in tasks:
            raise exceptions.ExistsException("Task does not exists.")
        while True:
            print(f"Task Edit\n1. Name\n2. Text\n3. Date\n4. Back")
            user_choice = int(input("Select: "))
            if user_choice == 1:
                #Add new name with text
                old_name = name
                text = tasks.get(old_name)
                new_name = get_name()
                tasks[new_name] = text
                #Add mark
                mark_new = mark.manage.get(old_name)
                mark.manage.add(tasks, new_name, mark_new)
                #Add date
                deadline_old = date.manage.get_deadline(old_name)
                
                #Pop out task with old name
                tasks.pop(old_name)
            elif user_choice == 2:
                text = get_text()
                tasks[name] = text
            elif user_choice == 3:
                print("change date in progress")
                #deadline_new = date.manage.set_deadline(new_name)
            elif user_choice == 4:
                break
    except Exception as e:
        print(f"Error: {e}")

def display(tasks):
    try:
        if len(tasks) == 0:
            raise exceptions.ExistsException("Task does not exists.")
        else:
            for task, text in tasks.items():
                print(task, "-", text, "-", mark.manage.get(task), "-", date.manage.remaining_days(task))
    except Exception as e:
        print(f"Error: {e}")

def clear(tasks):
    tasks.clear()

def select(tasks):
    try:
        name = input("Enter name of task to select: ")
        if name not in tasks:
            raise exceptions.ExistsException("Task not found.")
        return name, tasks[name]
    except Exception as e:
        print(f"Error: {e}")
        return None, None
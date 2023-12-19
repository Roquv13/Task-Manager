import exceptions
import mark_manage

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
        mark = mark_manage.get_mark(text)
        name[text] = mark
        print(f"Task '{name}' added.")
    except Exception as e:
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
        name, text = get_task()
        if name not in tasks:
            raise exceptions.ExistsException("Task does not exists.")
        tasks[name] = text
    except Exception as e:
        print(f"Error: {e}")

def display(tasks):
    try:
        if len(tasks) == 0:
            raise exceptions.ExistsException("Task does not exists.")
        else:
            for task, text in tasks.items():
                print(task, "-", text)
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
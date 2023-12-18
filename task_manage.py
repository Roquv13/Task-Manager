import exceptions

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
    
def add(tasks):
    try:
        name, text = get_task()
        if name in tasks:
            raise exceptions.ExistsException("Task already exists")
        tasks[name] = text
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
    for task, text in tasks.items():
        print(task, "-", text)

def clear(tasks):
    tasks.clear()
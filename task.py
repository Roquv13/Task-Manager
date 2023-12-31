import exceptions
import mark
import deadline
import exceptions
import sort_task

def get_name():
    name = input("Enter name of task: ")
    return name

def get_text():
    text = input("Enter text for task: ")
    return text

def task():
    try:
        name = get_name()
        text = get_text()
        return name, text
    except Exception as e:
        print(f"Error: {e}")

def get(tasks):
    if len(tasks) == 0:
            print("There is no task.")
    else:
        print("All of created tasks:")
        for name_task, task in tasks.items():
            print(name_task)
    
def add(tasks):
    try:
        name, text = task()
        if name in tasks:
            raise exceptions.ExistsException("Task already exists")
        tasks[name] = text
        deadline.set(name)
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
        while True:
            get(tasks)
            name = get_name()
            if name not in tasks:
                raise exceptions.ExistsException("Task does not exists.")
            print(f"Task Edit\n1. Name\n2. Text\n3. Date\n4. Back")
            user_choice = int(input("Select: "))
            if user_choice == 1:
                #Add new name with text
                old_name = name
                text = tasks.get(old_name)
                new_name = get_name()
                tasks[new_name] = text
                #Move mark
                mark.move(old_name, new_name, tasks)
                #Move date
                deadline_old = deadline.task_deadlines.get(old_name)
                deadline.add(new_name, deadline_old)
                deadline.delete(old_name)
                #Pop out task with old name
                tasks.pop(old_name)
                break
            elif user_choice == 2:
                text = get_text()
                tasks[name] = text
                break
            elif user_choice == 3:
                deadline.delete(name)
                deadline.set(name)
                break
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
                print(task, "-", text, "-", mark.get(task), "-", deadline.get_days(task))
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
    
def menu(name_list, selected_list):
    while True:
        try:    
            print(f"\nTask list '{name_list}'\n1. Add task\n2. Mark task\n3. Edit task\n4. Delete task\n5. Print tasks\n6. Sort tasks\n7. Clear tasks\n8. Back")
            user_choice = int(input("Select: "))
            if user_choice < 1 or user_choice > 7:
                raise exceptions.BadValue("Number must be in range from 1 to 6.")
            if user_choice == 1:
                add(selected_list)
            elif user_choice == 2:
                if len(selected_list) != 0:
                    mark.menu(selected_list)
            elif user_choice == 3:
                edit(selected_list)
            elif user_choice == 4:
                get(selected_list)
                delete(selected_list)
            elif user_choice == 5:
                display(selected_list)
            elif user_choice == 6:
                sort_task.menu(name_list, selected_list)
            elif user_choice == 7:
                clear(selected_list)
            elif user_choice == 8:
                break
        except Exception as e:
            print(f"Error: {e}")
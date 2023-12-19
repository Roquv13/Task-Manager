import task_manage
import exceptions

def interface(tasks):
    name_task, selected_task = task_manage.select(tasks) 
    while True:
        try:   
            print(f"\nMark task '{name_task}'\n1. Completed\n2. Not completed\n3. In progress\n4. Important\n5. Back")
            user_choice = int(input("Select: "))
            if user_choice < 1 or user_choice > 5:
                raise exceptions.BadValue("Number must be in range from 1 to 5.")
        except Exception as e:
            print(f"Error: {e}")

        if user_choice == 1:
            completed(name_task, selected_task)
        elif user_choice == 2:
            not_completed(name_task, selected_task)
        elif user_choice == 3:
            in_progress(name_task, selected_task)
        elif user_choice == 4:
            important(name_task, selected_task)
        elif user_choice == 5:
            break

completed_list = {}
not_completed_list = {}
in_progress_list = {}
important_list = {}

def completed(name_task, selected_task):
    try:
        completed_list[name_task] = selected_task
        print("Task marked as 'completed'")
        print(completed_list)
    except Exception as e:
        print(f"Error: {e}")

def not_completed(name_task, selected_task):
    try:
        not_completed_list[name_task] = selected_task
        print("Task marked as 'not completed'")
        print(not_completed_list)
    except Exception as e:
        print(f"Error: {e}")

def in_progress(name_task, selected_task):
    try:
        in_progress_list[name_task] = selected_task
        print("Task marked as 'in progress'")
        print(in_progress_list)
    except Exception as e:
        print(f"Error: {e}")

def important(name_task, selected_task):
    try:
        important_list[name_task] = selected_task
        print("Task marked as important")
        print(important_list)
    except Exception as e:
        print(f"Error: {e}")
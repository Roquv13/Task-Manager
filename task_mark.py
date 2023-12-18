import task_manage
import exceptions

completed_tasks = {}

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
            completed(name_task, selected_task, tasks)
        elif user_choice == 2:
            print("Not completed")
        elif user_choice == 3:
            print("In progress")
        elif user_choice == 4:
            print("Important")
        elif user_choice == 5:
            break

def completed(name_task, selected_task, tasks):
    try:
        completed_tasks[name_task] = selected_task
        tasks.pop(name_task)
        print("Task mark as completed")
        print(completed_tasks)
    except Exception as e:
        print(f"Error: {e}")
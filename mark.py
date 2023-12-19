import task_manage
import exceptions
import mark_manage

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
            mark_manage.completed(name_task, selected_task)
        elif user_choice == 2:
            mark_manage.not_completed(name_task, selected_task)
        elif user_choice == 3:
            mark_manage.in_progress(name_task, selected_task)
        elif user_choice == 4:
            mark_manage.important(name_task, selected_task)
        elif user_choice == 5:
            break
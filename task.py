import task_manage
import exceptions

def interface(name_list, selected_list):
    while True:
        try:    
            print(f"Task list '{name_list}'\n1. Add task\n2. Edit task\n3. Delete task\n4. Print tasks\n5. Clear tasks\n6. Exit")
            user_choice = int(input("Select: "))
            if user_choice < 1 or user_choice > 6:
                raise exceptions.BadValue("Number must be in range from 1 to 6.")
        except Exception as e:
            print(f"Error: {e}")

        if user_choice == 1:
            task_manage.add_task(selected_list)
        elif user_choice == 2:
            task_manage.edit_task(selected_list)
        elif user_choice == 3:
            task_manage.delete_task(selected_list)
        elif user_choice == 4:
            task_manage.print_task(selected_list)
        elif user_choice == 5:
            task_manage.clear_tasks(selected_list)
        elif user_choice == 6:
            break
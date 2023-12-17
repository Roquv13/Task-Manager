import task_manage
import exceptions

def interface(name_list, selected_list):
    while True:
        try:    
            print(f"\nTask list '{name_list}'\n1. Add task\n2. Edit task\n3. Delete task\n4. Print tasks\n5. Clear tasks\n6. Exit")
            user_choice = int(input("Select: "))
            if user_choice < 1 or user_choice > 6:
                raise exceptions.BadValue("Number must be in range from 1 to 6.")
        except Exception as e:
            print(f"Error: {e}")

        if user_choice == 1:
            task_manage.add(selected_list)
        elif user_choice == 2:
            task_manage.edit(selected_list)
        elif user_choice == 3:
            task_manage.delete(selected_list)
        elif user_choice == 4:
            task_manage.print(selected_list)
        elif user_choice == 5:
            task_manage.clear(selected_list)
        elif user_choice == 6:
            break
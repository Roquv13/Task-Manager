import task.manage as manage
import exceptions
import mark.interface as interface

def menu(name_list, selected_list):
    while True:
        try:    
            print(f"\nTask list '{name_list}'\n1. Add task\n2. Mark task\n3. Edit task\n4. Delete task\n5. Print tasks\n6. Clear tasks\n7. Back")
            user_choice = int(input("Select: "))
            if user_choice < 1 or user_choice > 7:
                raise exceptions.BadValue("Number must be in range from 1 to 6.")
            if user_choice == 1:
                manage.add(selected_list)
            elif user_choice == 2:
                if len(selected_list) != 0:
                    interface.menu(selected_list)
            elif user_choice == 3:
                manage.get_tasks(selected_list)
                manage.edit(selected_list)
            elif user_choice == 4:
                manage.get_tasks(selected_list)
                manage.delete(selected_list)
            elif user_choice == 5:
                manage.display(selected_list)
            elif user_choice == 6:
                manage.clear(selected_list)
            elif user_choice == 7:
                break
        except Exception as e:
            print(f"Error: {e}")
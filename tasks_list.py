import exceptions
import task

def create(lists):
    try:
        list_name = input("Enter name of list: ")
        if list_name in lists:
            raise exceptions.ExistsException("List already exists.")
        lists[list_name] = {}
        print(f"List '{list_name}' created.")
        task.menu(list_name, lists[list_name])
    except Exception as e:
        print(f"Error: {e}")

def select(lists):
    try:
        list_name = input("Enter name of list to select: ")
        if list_name not in lists:
            raise exceptions.ExistsException("List not found.")
        return list_name, lists[list_name]
    except Exception as e:
        print(f"Error: {e}")
        return None, None
    
def delete(lists):
    get_lists()
    try:
        list_name = input("Enter name of list to delete or type EXIT: ")
        if list_name.upper() == "EXIT":
            pass
        elif list_name not in lists:
            raise exceptions.ExistsException("List not found.")
        else:
            lists.pop(list_name)
            print(f"List '{list_name} deleted.'")
    except Exception as e:
        print(f"Error: {e}")

def get_lists(lists):
    if len(lists) == 0:
        print("There is no list.")
    else:
        print("All of created lists:")
        for name_list, list in lists.items():
            print(name_list)

def menu(lists):
    while True:
        print("\nUser Menu\n1. Create a new list\n2. Select list\n3. Delete list\n4. Names of lists\n5. Exit")
        try:
            choice_int = int(input("Enter number: "))
            if choice_int < 1 or choice_int > 5:
                raise exceptions.BadValue("Number must be in range 1 to 5.")
            if choice_int == 1:
                create(lists)
            elif choice_int == 2:
                get_lists(lists)
                name_list, selected_list = select(lists)
                task.menu(name_list, selected_list)
            elif choice_int == 3:
                delete(lists)
            elif choice_int == 4:
                get_lists(lists)
            elif choice_int == 5:
                break
        except Exception as e:
            print(f"Error: {e}")
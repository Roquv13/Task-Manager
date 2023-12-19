import exceptions

def create(lists):
    try:
        list_name = input("Enter name of list: ")
        if list_name in lists:
            raise exceptions.ExistsException("List already exists.")
        lists[list_name] = {}
        print(f"List '{list_name}' created.")
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
def create_list():
    try:
        list_name = input("Enter name of list: ")
    except Exception as e:
        print(f"Error: {e}")
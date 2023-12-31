import exceptions
#Functions
def name(tasks):
    return dict(sorted(tasks.items()))

def text(tasks):
    return dict(sorted(tasks.items(), key=lambda item: item[1]))

def menu(name_list, selected_list):
    while True:
        try:    
            print(f"\nTask list '{name_list} sort by: '\n1. Name\n2. Text\n3. Back")
            user_choice = int(input("Select: "))
            if user_choice < 1 or user_choice > 3:
                raise exceptions.BadValue("Number must be in range from 1 to 3.")
            if user_choice == 1:
                selected_list = name(selected_list)
            elif user_choice == 2:
                selected_list = text(selected_list)
            elif user_choice == 3:
                break
        except Exception as e:
            print(f"Error: {e}")

#Test
tasks = {3: "bacd", 1: "abcd", 2: "cabd"}
print (tasks)

tasks = text(tasks)
print(tasks)
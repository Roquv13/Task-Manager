#Functions
def name(tasks):
    return dict(sorted(tasks.items()))

def text(tasks):
    return dict(sorted(tasks.items(), key=lambda item: item[1]))

def menu(tasks):
    

#Test
tasks = {3: "bacd", 1: "abcd", 2: "cabd"}
print (tasks)

tasks = text(tasks)
print(tasks)
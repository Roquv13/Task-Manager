#Functions
def name(tasks):
    return dict(sorted(tasks.items()))

def text(tasks):
    

#Test
tasks = {3: "bacd", 1: "abcd", 2: "cabd"}
print (tasks)

tasks = text(tasks)
print(tasks)
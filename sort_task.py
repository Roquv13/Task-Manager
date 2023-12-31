#Functions
def name(tasks):
    return dict(sorted(tasks.items()))

#Test
tasks = {3: "abcd", 1: "bacd", 2: "cabd"}
print (tasks)

tasks = name(tasks)
print(tasks)
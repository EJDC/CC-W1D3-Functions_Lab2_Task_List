# Task list as provided in start code.

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# FUNCTIONS
# 1. Print a list of uncompleted tasks
def uncompleted():
    for task in tasks:
        if task["completed"] == False:
            print(task)

# 2. Print a list of completed tasks
def completed():
    for task in tasks:
        if task["completed"] == True:
            print(task)

# 3. Print a list of all task descriptions
def all_descriptions():
    for task in tasks:
        print(task["description"])

# 4. Print a list of tasks where time_taken is at least a given time
def twenty_mins():
    for task in tasks:
        if task["time_taken"] >= 20:
            print(task)

# 5. Print any task with a given description
def description_is():
    user_input = input("What is the description?\n")
    searched_task = ""
    for task in tasks:
        if task["description"] == user_input:
            searched_task = task
    print()
    if searched_task == "":
        print("Could not find task matching that description!  Please try again.")
    else:
        print(task)

# 6. Given a description update that task to mark it as complete.
def mark_completed():
    user_input = input("What is the description of the task that you've completed?\n")
    searched_task = False
    print()
    for task in tasks:
        if task["description"] == user_input:
            searched_task = True
            task["completed"] = True
            print(task["description"] + " task completion status is now set to: " + str(task["completed"]))
    if searched_task == False:
        print("Could not find task matching that description!")

# 7. Add a task to the list
def add_task():
    new_task_description = input("What's the name of the task you'd like to add?\n")
    print()
    try:
        new_task_time = int(input("How much time will it take in minutes?\n"))
    except ValueError:
        print("Your selection must be an integer please!")
        exit()
    print()
    tasks.append({"description": new_task_description, "completed": False, "time_taken": new_task_time})
    print(new_task_description + " has been added to the list, with an estimated time of " + str(new_task_time) + " mins")

# MAIN PROGRAM
# Print welcome and options
print()
print("Welcome!  Please select what you would like to do!")
print()
print("1. Print a list of uncompleted tasks")
print("2. Print a list of completed tasks")
print("3. Print a list of all task descriptions")
print("4. Print a list of tasks where estimated time is at least 20 mins")
print("5. Print task based on description")
print("6. Update a task to mark it as complete.")
print("7. Add a task to the list")
print()

# Try to get a valid integer input from the user, otherwise exit.
try:
    option = int(input('Type a number from the list and press return to select!\n'))
except ValueError:
    print("Your selection must be an integer please!")
    exit()

# If the option doesn't exist, then exit.
if option > 7 or option < 1:
    print("This is an invalid option.  Please select from options above")
    exit()

print()

# Direct user to correct function.
if option == 1:
    uncompleted()
elif option == 2:
    completed()
elif option == 3:
    all_descriptions()
elif option == 4:
    twenty_mins()
elif option == 5:
    description_is()
elif option == 6:
    mark_completed()
elif option == 7:
    add_task()

print()
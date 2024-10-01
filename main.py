import json
import time


def decorator_info(func):
    def wrapper(*args, **kwargs):
        print('=' * 23, 'List of tasks', '=' * 23)
        func(*args, **kwargs)
        print('=' * 23, 'End of tasks', '=' * 23, '\n')

    return wrapper

# Class
class ToDoList:
    """Imitating a ToDo list"""

    def __init__(self):
        """Initialize the attributes of the ToDo list"""
        self.todos_list = []

    def add_task(self, to_do_task):
        """Add a task to the ToDo list"""
        self.todos_list.append(to_do_task)

    def remove_task(self, task_index):
        """Remove a task from the ToDo list"""
        if 1 <= task_index <= len(self.todos_list):
            del self.todos_list[task_index - 1]
        else:
            print("No such task found, try again!")

    def marked_as_completed(self, task_index):
        """Mark the ToDo list as completed"""
        # We need to find index of sentence
        if 1 <= task_index <= len(self.todos_list):
            self.todos_list[task_index - 1] += ' - Completed'

    def save_to_json(self):
        """Saves the ToDo list to a json file"""
        with open("todos.json", "w") as file:
            json.dump(self.todos_list, file)

    def load_to_json(self, json_file):
        """Loads the ToDo list from a json"""
        try:
            with open(json_file, "r") as file:
                self.todos_list = json.load(file)
        except FileNotFoundError:
            print("No such file found, try again!")

    @decorator_info
    def get_todos(self):
        """Get all the tasks in the ToDo list"""
        for index, values in enumerate(self.todos_list, start=1):
            print(f"{index}. {values.capitalize()}")


# Making an example of list
sample = ToDoList()
while True:

    print('-' * 25, "Main Menu", '-' * 25)
    print("1. Add")
    print("2. Delete")
    print("3. Marked")
    print("4. Save")
    print("5. Load")
    print("6. Show")
    print("7. Exit")
    example = input("Enter your choice: ")
    print('-' * 61)

    if example == '1':
        task = input("Enter a task to add: ")
        sample.add_task(task)
        print("Added")
        time.sleep(1)
        continue

    elif example == '2':
        rem = int(input("Enter a task you want to remove: "))
        sample.remove_task(rem)
        print("Removed")
        continue

    elif example == '3':
        mark = int(input("Enter a task you want to complete: "))
        sample.marked_as_completed(mark)
        print("Successfully completed")
        continue

    elif example == '4':
        sample.save_to_json()
        print("File successfully saved.")
        time.sleep(1)
        continue

    elif example == '5':
        file = input("Enter a file name: ")
        sample.load_to_json(file)
        print("Successfully loaded")
        time.sleep(1)
        continue

    elif example == '6':
        sample.get_todos()
        input("Press Enter to back to main menu...")
        continue

    elif example == '7':
        ask = input("Do you want to save? yes/no ")
        if ask == 'yes':
            sample.save_to_json()
            print("File successfully saved.")
            print("Bye! bye")
            time.sleep(1)
            break
        elif ask == 'no':
            print("Bye bye!")
            time.sleep(1)
            break
        else:
            print("Invalid entry. Please try again.")
            continue
    else:
        print("Invalid input entered!")
        continue

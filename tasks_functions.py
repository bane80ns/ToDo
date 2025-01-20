from methods import load_file, save_file
from datetime import datetime


def validate_due_date(date_str):
    try:
        due_date = datetime.strptime(date_str, "%Y-%m-%d")
        return due_date.strftime("%Y-%m-%d")  # Return as a string
    except ValueError:
        return None

def main_menu():
    # Displays the main menu and check for validation input
    while True:
        try:
            print("\nMake a choice what you need to do:\n"
                  "==================================\n"
                  "==================================")
            choice = int(input("1. Add Task\n2. View Tasks\n3. List tasks by priority \n4. View Tasks with full details\n5. Remove Task\n0. Exit\n: "))
            if choice in [0, 1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid choice. Please enter 0, 1, 2, 3, 4 or 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_task(tasks):
    # add task to a task list

    # adds task name to temp dict
    task_name = input("\nName your task: ")

    # adds task desc to temp dict
    task_description = input("\nDescription of your task: ")

    # check for first free id in tasks and add it to temp dic
    for task_id in tasks.items():
        task_id_new = int(task_id[0]) + 1

    # requesting task priority from user and adding to temp dict
    task_priority = None
    while not task_priority in ["1", "2", "3"]:
        task_priority = input("\nChoose your task's priority (1 - High, 2 - Medium, 3 - Low): ")
        if task_priority == "1":
            task_prio = "High"
        elif task_priority == "2":
            task_prio = "Medium"
        else:
            task_prio = "Low"

    # date input and validation
    due_date = None
    while not due_date:
        due_date_input = input("\nEnter Due date in format YYYY-MM-DD: ")
        due_date = validate_due_date(due_date_input)
        if not due_date:
            print("Invalid date format. Please use YYYY-MM-DD.")

    print(due_date)

    # new temporary task dictionary that will be added into json
    new_task_dict = {
        str(task_id_new): {
            "id": str(task_id_new),
            "name": task_name,
            "description": task_description,
            "priority": task_prio,
            "due_date": due_date
        }
    }

    #print("\n", new_task_dict)
    tasks.update(new_task_dict)
    save_file("data/tasks.json", tasks)
    print(f"Task '{task_name}' added.")


def view_tasks(tasks):
    # Print tasks from list (tasks)
    if tasks:
        print("\nHere is the list of tasks:\n"
              "**************************")
        for value in tasks.values():
            print(f"#{value["id"]}: {value["name"]}")
    else:
        print("\nNo tasks available.")


def view_tasks_by_prio(tasks):
    # View tasks sorted by priority
    priority_order = {"High" : 1, "Medium": 2, "Low": 3}

    sorted_tasks = sorted(
        tasks.items(),
        key=lambda item: priority_order[item[1]["priority"]],
    )




    if tasks:
        print("\nHere is the list of tasks:\n"
              "*******************************************")
        # print(sorted_tasks)
        for task_id, task_details in sorted_tasks:
            task_id, name, description, priority, due_date = (
                task_details["id"],
                task_details["name"],
                task_details["description"],
                task_details["priority"],
                task_details["due_date"],

            )

            print(f"#{task_id:2} # {task_details["name"]:<20} Priority :{task_details["priority"]}")
    else:
        print("\nNo tasks available.")


def view_tasks_full(tasks):
    # View tasks with full details

    if tasks:
        print("\nHere is the list of tasks:\n"
              "*******************************************")
        # print(sorted_tasks)
        for task_id, task_details in tasks.items():
            task_id, name, description, priority, due_date = (
                task_details["id"],
                task_details["name"],
                task_details["description"],
                task_details["priority"],
                task_details["due_date"],

            )

            print(f"#{task_id:2}# {task_details["name"]:<18} Priority :{task_details["priority"]:10} DUE DATE: {task_details['due_date']:21}  Description: {task_details['description']}")
    else:
        print("\nNo tasks available.")


def remove_task(tasks):
    # Remove task from task list, but first checks if tasks list is not empty
    # Validate task input
    if not tasks:
        print("\nNo tasks to remove.")
        return

    view_tasks(tasks)
    while True:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            key_list = []

            for key, value in tasks.items():
                # print(f"{key} : {value['name']}")
                key_list.append(key)


            if len(key_list) == 0:
                 print("\nNo tasks to remove.")
                 break

            elif str(task_number) in key_list:

                print(f"Task '{tasks[str(task_number)]["name"]}' removed.")
                del tasks[str(task_number)]
                save_file("data/tasks.json", tasks)

                break
            else:
                print("Task number out of range. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")





# To-Do App
# from methods.py load def load_file
from methods import load_file, save_file
from tasks_functions import *


def main():
    print("Hello...\nWelcome to the TO-DO List app:\n******************************\n")


    tasks = load_file("data/tasks.json")


    while True:
        choice = main_menu()

        if choice == 1:
            add_task(tasks)

        elif choice == 2:
            view_tasks(tasks)


        elif choice == 3:
            view_tasks_by_prio(tasks)


        elif choice == 4:
            view_tasks_full(tasks)

        elif choice == 5:
            remove_task(tasks)


        elif choice == 0:
            print("Thank you for using TaskMaster\n"
                  "Made by Branislav Pekar\n"
                  "Goodbye!!!")
            break


if __name__ == "__main__":
    main()

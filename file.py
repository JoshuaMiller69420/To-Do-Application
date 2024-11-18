import json

class bcolors:
    ENDC = '\033[0m'
    WARNING = '\033[93m'


def load_tasks():
    with open("tasks.json", "r") as file:
        data = json.load(file)
        return


def menu():
    user_in = str(input(f"{bcolors.WARNING}{"Choose one of the options below"}{bcolors.ENDC} \n1. View completed tasks \n2. View incomplete tasks \n3. View all tasks \n4. Mark a task as complete \n5. Add a new task \n6. Exit \n1-6:"))


def main():
    load_tasks()
    data = load_tasks()
    menu()
    


if __name__ == "__main__":
    main()
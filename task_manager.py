import json

def save_tasks_to_file(tasks, filename):
    """Save tasks to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def load_tasks_from_file(filename):
    """Load tasks from a JSON file."""
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]

if __name__ == "__main__":
    tasks = [
        {"Id":"id","title": "Task 1","Completed":"False"},
        {"Id":"id","title": "Task 2","Completed":"True"}
    ]

    save_tasks_to_file(tasks,'tasks.json')

    loaded_tasks = load_tasks_from_file(tasks,'tasks.json')
    print(loaded_tasks)

tasks = []

def create_tasks():
    ID = int(input("Enter Your Tasks ID: "))
    Title = str(input("Enter Your Tasks Title: "))
    Completed = bool(input("Enter Your Tasks Completed: "))
    tasks.append({"Task ID":ID, "Task Title": Title, "Task Completed": Completed})
    print("Task Created Successfully.")

def view_tasks():
    if tasks:
        print("Available Tasks: ")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx} Task ID:{task['Task ID']}, Task Title: {task['Task Title']}, Task Completed: {task['Task Completed']}")
    else:
        print("No Tasks are Available...")

def delete_tasks():
    view_tasks()
    if tasks:
        tasks_index =int(input("Enter the index of the task to be deleted: ")) -1
        if 0<= tasks_index < len(tasks):
            deleted_task = tasks.pop(tasks_index)
            print(f"Task '{deleted_task['Task Title']}' deleted successfully.")
        else:
            print("This is an Invalid task index.")
    else:
        print("There are no tasks available.")

def update_tasks():
    view_tasks()
    if tasks:
        tasks_index = int(input("Enter the Index of your task to be updated: ")) -1
        if 0 <= tasks_index < len(tasks):
            new_task_id = int(input("Enter your new Id or (Please  Enter to keep current Id):"))
            new_task_title = str(input("Enter your new Id or (Please  Enter to keep current Id):"))
            new_task_complete = bool(input("Enter your new Id or (Please  Enter to keep current Id):"))
            if new_task_id:
                tasks[tasks_index]['Task Id'] = new_task_id
            if new_task_title:
                tasks[tasks_index]['Task Title'] = new_task_title
            if new_task_complete:
                tasks[tasks_index]['Task Complete'] = new_task_complete
            print("Your Tasks has been updated")
        else:
            print("Invalid Response. Please try again.")
    else:
        print("There are no tasks available.")

while True:
    print("\n Welcome to the interactive task manager..")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Select an option from (1-5): ")

    if choice == '1':
        create_tasks()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_tasks()
    elif choice == '4':
        update_tasks()
    elif choice == '5':
        print("Exiting the task manager.")
        break
    else:
        print("Invalid option. Please select between 1 and 5.")

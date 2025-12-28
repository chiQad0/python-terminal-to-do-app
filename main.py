import json

# To-do-list terminal app

def add_task(task: list):
    title = input("Enter a task: ").strip()

    if not title:
        print("Task cannot be empty")
        return

    task.append({"title": title, "done": False})
    save_tasks(task)
    print("Task added successfully")

def list_task(task: list):
    if not task:
        print("No tasks available")
        return

    for i, t in enumerate(task, start=1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']}")

def remove_task(task: list):
    list_task(task)
    if not task:
        return

    try:
        index = int(input("Enter task number to remove: ")) - 1
        removed = task.pop(index)
        save_tasks(task)
        print(f"Removed: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid task number")

def mark_task_done(task: list):
    list_task(task)
    if not task:
        return

    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        task[index]["done"] = True
        save_tasks(task)
        print("Task marked as done")
    except (ValueError, IndexError):
        print("Invalid task number")

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(task, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(task, file, indent=4)


task = load_tasks()

while True:
    print("\nChoose an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

    choice = input("> ").strip()

    if choice == "1":
        add_task(task)
    elif choice == "2":
        list_task(task)
    elif choice == "3":
        mark_task_done(task)
    elif choice == "4":
        remove_task(task)
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid option")





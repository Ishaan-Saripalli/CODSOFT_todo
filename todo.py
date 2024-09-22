import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task['completed'] else "Pending"
        print(f"{i}. {task['title']} - {status}")
        if task['description']:
            print(f"   Description: {task['description']}")
        if task['due_date']:
            print(f"   Due Date: {task['due_date']}")
    print()

def add_task(tasks):
    title = input("Enter the task title: ")
    description = input("Enter the task description (optional): ")
    due_date = input("Enter the due date (optional): ")
    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully!")

def update_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        task = tasks[task_num]
        print(f"Updating Task: {task['title']}")
        task['title'] = input(f"Enter the new title (current: {task['title']}): ") or task['title']
        task['description'] = input(f"Enter the new description (current: {task['description']}): ") or task['description']
        task['due_date'] = input(f"Enter the new due date (current: {task['due_date']}): ") or task['due_date']
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        task = tasks.pop(task_num)
        save_tasks(tasks)
        print(f"Task '{task['title']}' deleted successfully!")
    else:
        print("Invalid task number!")

def mark_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to mark as complete/incomplete: ")) - 1
    if 0 <= task_num < len(tasks):
        task = tasks[task_num]
        task['completed'] = not task['completed']
        save_tasks(tasks)
        status = "completed" if task['completed'] else "pending"
        print(f"Task '{task['title']}' marked as {status}!")
    else:
        print("Invalid task number!")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete/Incomplete")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task(tasks)
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    
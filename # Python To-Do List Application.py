# Python To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def update_task(index, updated_task):
    if 0 < index <= len(tasks):
        tasks[index - 1] = updated_task
        print(f"Task {index} updated.")
    else:
        print("Invalid task index.")

def remove_task(index):
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")

if __name__ == "__main__":
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Update Task\n4. Remove Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            index = int(input("Enter the index of the task to update: "))
            updated_task = input("Enter updated task: ")
            update_task(index, updated_task)
        elif choice == "4":
            show_tasks()
            index = int(input("Enter the index of the task to remove: "))
            remove_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

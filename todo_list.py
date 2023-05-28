import os

# Function to clear the terminal screen
def clear_screen():
    os.system('clear')

# Function to display the to-do list
def display_list(todo_list):
    clear_screen()
    print("To-Do List:")
    print("-----------")
    if len(todo_list) == 0:
        print("No tasks.")
    else:
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter task: ")
    todo_list.append(task)
    print("Task added successfully!")

# Function to remove a task from the to-do list
def remove_task(todo_list):
    display_list(todo_list)
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")

# Main function
def main():
    todo_list = []
    while True:
        clear_screen()
        print("To-Do List Manager")
        print("------------------")
        print("1. Display the to-do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            display_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

if __name__ == '__main__':
    main()

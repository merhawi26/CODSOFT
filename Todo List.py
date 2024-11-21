# Task 1:  Todo List Project


# Read the current task list from a file
def read_from_file(filename="Todo List.txt"):
    try:
        with open(filename) as file:
            # Reads the entire file then, return a list containing tasks
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist


# Write the updated task list to a file
def write_to_file(tasks, filename="Todo List.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


# Add a new task to the task list
def add_task(task_list):
    new_task = input("Enter the new task: ").strip().capitalize()
    if new_task:
        # add the new tasks to a list
        task_list.append(new_task)
        # then write the list into file
        write_to_file(task_list)
        print("%%%%% Task added successfully %%%%%")
    else:
        print("Task cannot be empty!")


# View all tasks in the task list
def view_tasks(task_list):
    if task_list:
        print("Your Tasks:")
        # idx used to give number list for the tasks, start from 1
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display. Add some tasks!")


# Mark a task as completed
def task_completed(task_list):
    if not task_list:
        print("No tasks to complete. Add some tasks first!")
        return

    view_tasks(task_list)
    completed_task_number = int(input("Enter the task number you have completed : "))
    try:
        if 1 <= completed_task_number <= len(task_list):
            print(
                f"Task '{task_list.pop((completed_task_number - 1))}' marked as completed!"
            )
            write_to_file(task_list)

        else:
            print(f"Invalid task number : {completed_task_number}")
    except ValueError:
        print("Please, enter a valid number ")


# Display the main menu
def menu():
    task_list = read_from_file()
    while True:
        print("\n======= Welcome to My Todo List 📋 =======")
        try:
            user_input = int(
                input(
                    "1. Add a Task 📝\n2. View Tasks 📜\n3. Mark a Task as Completed ✔ \n4. Exit\nEnter your option: "
                )
            )
            if user_input == 1:
                add_task(task_list)
            elif user_input == 2:
                view_tasks(task_list)
            elif user_input == 3:
                task_completed(task_list)
            elif user_input == 4:
                print("Thanks! Bye Bye")
                break
            else:
                print("Invalid choice, please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    menu()

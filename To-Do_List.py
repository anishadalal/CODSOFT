class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})
        print("Task added!")

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            status = "\u2705" if task["completed"] else "\u274C"
            print(f"{idx}. {status} {task['description']}")

    def mark_task_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted.")
        else:
            print("Invalid task number!")

    def save_tasks(self):
        try:
            with open("tasks.txt", "w") as file:
                for task in self.tasks:
                    # Save task info as strings separated by a comma
                    status = "completed" if task["completed"] else "pending"
                    file.write(f"{task['description']},{status}\n")
            print("Tasks saved successfully!")
        except Exception as e:
            print(f"Failed to save tasks: {e}")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = []
                for line in file:
                    description, status = line.strip().split(",")
                    self.tasks.append({"description": description, "completed": status == "completed"})
            print("Tasks loaded.")
        except FileNotFoundError:
            print("No saved tasks found. Starting fresh.")
        except Exception as e:
            print(f"Failed to load tasks: {e}")

def display_menu():
    print("\nChoose an option:")
    print("1. View To-Do List")
    print("2. Add a New Task")
    print("3. Mark a Task as Complete")
    print("4. Delete a Task")
    print("5. Save Tasks")
    print("6. Exit")

def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.list_tasks()
        elif choice == "2":
            description = input("\nEnter the task description: ").strip()
            if description:
                manager.add_task(description)
            else:
                print("Task description cannot be empty!")
        elif choice == "3":
            manager.list_tasks()
            try:
                task_num = int(input("\nEnter the task number to mark as complete: "))
                manager.mark_task_complete(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            manager.list_tasks()
            try:
                task_num = int(input("\nEnter the task number to delete: "))
                manager.delete_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            manager.save_tasks()
        elif choice == "6":
            manager.save_tasks()
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()

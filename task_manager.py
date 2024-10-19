# Import the json to handle JSON file operations
import json

# Class represents a single task with id, title and completed status
class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

# Class having all features like load, save, add, view,delete, and mark tasks as completed.
class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    # Load tasks from json file
    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
            
            if not tasks_data:
                print(f"No tasks found in {self.filename}. Starting with an empty task list.")
                return

            self.tasks = []
            for task_data in tasks_data:
                task = Task(task_data['id'], task_data['title'], task_data['completed'])
                self.tasks.append(task)
            print(f"Tasks loaded from {self.filename}")
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty task list.")
        except json.JSONDecodeError:
            print(f"Error reading {self.filename}. File may be empty or corrupt. Starting with an empty task list.")   

    # Save tasks to json file
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        print(f"Tasks saved to {self.filename}")
    
    # Add task 
    def add_task(self, title):
        new_id = max([task.id for task in self.tasks], default=0) + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        print(f"Task added: {title}")
        self.save_tasks()

    # View Task
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"ID: {task.id}, Title: {task.title}, Status: {status}")

    # Delete task
    def delete_task(self, task_id):
        task_id = int(task_id)
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task deleted: {task.title}")
                self.save_tasks()
                return
        print("Task not found.")

    #Mark task as completed
    def mark_completed(self, task_id):
        task_id = int(task_id)
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Task marked as completed: {task.title}")
                self.save_tasks()
                return
        print("Task not found.")



# Main Funcction
def main():
    task_manager = TaskManager()

    # Display menu options
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Handle user input
        if choice == '1':
            title = input("Enter task title: ")
            task_manager.add_task(title)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_id = input("Enter task ID to delete: ")
            task_manager.delete_task(task_id)
        elif choice == '4':
            task_id = input("Enter task ID to mark as completed: ")
            task_manager.mark_completed(task_id)
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

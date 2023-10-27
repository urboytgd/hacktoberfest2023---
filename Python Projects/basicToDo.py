class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def complete(self):
        self.is_completed = True

    def __str__(self):
        return "[X]" + self.description if self.is_completed else "[ ]" + self.description


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
        else:
            print("Invalid index!")

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")


def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List App")
        print("1. Add task")
        print("2. Complete task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            to_do_list.add_task(description)

        elif choice == "2":
            index = int(input("Enter task number to mark as complete: ")) - 1
            to_do_list.complete_task(index)

        elif choice == "3":
            to_do_list.display_tasks()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

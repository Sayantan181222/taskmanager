import sys
from tasks import add_task
from display import show_all_tasks, show_task_count
from storage import load_tasks, save_tasks, delete_task

def main():
    print("Task Manager v1.0")
    print("------------------")
    tasks = load_tasks()

    if len(sys.argv) < 2:
        show_all_tasks(tasks)
        show_task_count(tasks)
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        title = " ".join(sys.argv[2:])
        tasks = add_task(tasks, title)
        save_tasks(tasks)
    elif command == "list":
        show_all_tasks(tasks)
        show_task_count(tasks)
    elif command == "delete" and len(sys.argv) > 2:
        try:
            task_id = int(sys.argv[2])
            tasks = delete_task(tasks, task_id)
            save_tasks(tasks)
        except ValueError:
            print("Error: task ID must be a number.")

if __name__ == "__main__":
    main()
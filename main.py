# main.py — updated by Sayan on feature/add-task
import sys
from tasks import add_task
from display import show_all_tasks, show_task_count
from storage import load_tasks, save_tasks

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
    else:
        print(f"Unknown command: {command}")
        print("Usage: python main.py add 'task title'")
        print("       python main.py list")

if __name__ == "__main__":
    main()
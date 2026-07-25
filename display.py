# display.py — Satyam
# Handles displaying tasks in the terminal

def show_all_tasks(tasks):
    """Display all tasks with status icons, IDs, and titles."""
    if not tasks:
        print("No tasks yet. Add one with: python main.py add 'your task'")
        return
    print("\nYour tasks:")
    print("-----------")
    for task in tasks:
        status_icon = "[x]" if task["status"] == "done" else "[ ]"
        print(f"  {status_icon} [{task['id']}] {task['title']}")
    print()

def show_task_count(tasks):
    """Print a summary line: done/total tasks completed."""
    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "done")
    pending = total - done
    print(f"  {done}/{total} completed  |  {pending} pending")

def show_single_task(task):
    """Display details for one specific task."""
    if not task:
        print("Task not found.")
        return
    status_label = "Done" if task["status"] == "done" else "Pending"
    print(f"\nTask [{task['id']}]: {task['title']}")
    print(f"  Status: {status_label}")
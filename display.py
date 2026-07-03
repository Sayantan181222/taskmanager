# display.py — Satyam
# Handles displaying tasks to the user

def show_all_tasks(tasks):
    """Display all tasks with their status and ID."""
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour tasks:")
    print("-----------")
    for task in tasks:
        status_icon = "[x]" if task["status"] == "done" else "[ ]"
        print(f"  {status_icon} [{task['id']}] {task['title']}")

def show_task_count(tasks):
    """Print a summary of completed vs total tasks."""
    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "done")
    print(f"\n{done}/{total} tasks completed")
# storage.py — Anant
# Handles reading, writing, and deleting tasks in JSON storage

import json
import os

STORAGE_FILE = "data/tasks.json"

def load_tasks():
    """Load tasks from JSON storage. Returns empty list if missing or corrupted."""
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted. Starting fresh.")
        return []

def save_tasks(tasks):
    """Save task list to JSON storage."""
    os.makedirs("data", exist_ok=True)
    try:
        with open(STORAGE_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def delete_task(tasks_list, task_id):
    """Remove a task by ID. Returns updated list."""
    original_len = len(tasks_list)
    updated = [t for t in tasks_list if t["id"] != task_id]
    if len(updated) == original_len:
        print(f"Error: no task with ID {task_id} found.")
    else:
        print(f"Deleted task [{task_id}].")
    return updated
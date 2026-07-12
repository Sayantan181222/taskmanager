# storage.py — Anant
# Handles reading and writing tasks to tasks.json

import json
import os

STORAGE_FILE = "data/tasks.json"

def load_tasks():
    """Load tasks from JSON storage file. Returns empty list if file missing."""
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted. Starting fresh.")
        return []

def save_tasks(tasks):
    """Save task list to JSON storage file."""
    os.makedirs("data", exist_ok=True)
    try:
        with open(STORAGE_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
        print(f"Saved {len(tasks)} task(s).")
    except IOError as e:
        print(f"Error saving tasks: {e}")
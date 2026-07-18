# tasks.py — Sayantan
# Task data model and task management logic

class Task:
    def __init__(self, task_id, title, status="pending"):
        self.task_id = task_id
        self.title = title
        self.status = status

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "status": self.status
        }

    def mark_done(self):
        self.status = "done"

    def __repr__(self):
        return f"Task({self.task_id}, '{self.title}', {self.status})"


def add_task(tasks_list, title):
    """Create a new task and append it to the task list."""
    if not title or not title.strip():
        print("Error: task title cannot be empty.")
        return tasks_list
    new_id = max((t["id"] for t in tasks_list), default=0) + 1
    new_task = Task(new_id, title.strip())
    tasks_list.append(new_task.to_dict())
    print(f"Added task [{new_id}]: {title.strip()}")
    return tasks_list
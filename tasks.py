# tasks.py — Sayantan
# Task data model

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

    def __repr__(self):
        return f"Task({self.task_id}, '{self.title}', {self.status})"
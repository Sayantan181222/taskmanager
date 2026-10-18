# tests/test_tasks.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tasks import Task, add_task

def test_task_creation():
    """Task object should store id, title, and default status."""
    t = Task(1, "Buy groceries")
    assert t.task_id == 1
    assert t.title == "Buy groceries"
    assert t.status == "pending"

def test_task_to_dict():
    """to_dict should return correct dictionary structure."""
    t = Task(2, "Study Git", "done")
    d = t.to_dict()
    assert d["id"] == 2
    assert d["title"] == "Study Git"
    assert d["status"] == "done"

def test_add_task_empty_list():
    """add_task on empty list should create task with ID 1."""
    result = add_task([], "First task")
    assert len(result) == 1
    assert result[0]["id"] == 99
    assert result[0]["title"] == "First task"

def test_add_task_auto_increment():
    """add_task should auto-increment ID based on existing tasks."""
    existing = [{"id": 1, "title": "Old task", "status": "pending"}]
    result = add_task(existing, "New task")
    assert result[-1]["id"] == 2

def test_add_task_empty_title():
    """add_task with empty title should reject and return unchanged list."""
    result = add_task([], "")
    assert len(result) == 0

def test_task_mark_done():
    """mark_done should change status to done."""
    t = Task(1, "Test task")
    t.mark_done()
    assert t.status == "done"
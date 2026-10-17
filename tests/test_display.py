# tests/test_display.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from display import show_all_tasks, show_task_count, show_single_task

def test_show_all_tasks_empty(capsys):
    """Empty task list should print no tasks message."""
    show_all_tasks([])
    captured = capsys.readouterr()
    assert "No tasks" in captured.out

def test_show_all_tasks_with_tasks(capsys):
    """Tasks should be displayed with status icons."""
    tasks = [
        {"id": 1, "title": "Buy groceries", "status": "pending"},
        {"id": 2, "title": "Study Git", "status": "done"}
    ]
    show_all_tasks(tasks)
    captured = capsys.readouterr()
    assert "[ ]" in captured.out
    assert "[x]" in captured.out
    assert "Buy groceries" in captured.out

def test_show_task_count(capsys):
    """Task count should show correct done/total ratio."""
    tasks = [
        {"id": 1, "title": "Task 1", "status": "done"},
        {"id": 2, "title": "Task 2", "status": "pending"}
    ]
    show_task_count(tasks)
    captured = capsys.readouterr()
    assert "1/2" in captured.out

def test_show_single_task_not_found(capsys):
    """None task should print not found message."""
    show_single_task(None)
    captured = capsys.readouterr()
    assert "not found" in captured.out
# tests/test_storage.py
import sys
import os
import json
import tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import storage

def test_load_tasks_missing_file(tmp_path, monkeypatch):
    """load_tasks should return empty list when file does not exist."""
    monkeypatch.setattr(storage, "STORAGE_FILE", str(tmp_path / "tasks.json"))
    result = storage.load_tasks()
    assert result == []

def test_save_and_load_tasks(tmp_path, monkeypatch):
    """save_tasks then load_tasks should return same data."""
    monkeypatch.setattr(storage, "STORAGE_FILE", str(tmp_path / "tasks.json"))
    tasks = [{"id": 1, "title": "Test", "status": "pending"}]
    storage.save_tasks(tasks)
    loaded = storage.load_tasks()
    assert loaded == tasks

def test_delete_task_existing(tmp_path, monkeypatch):
    """delete_task should remove task with matching ID."""
    monkeypatch.setattr(storage, "STORAGE_FILE", str(tmp_path / "tasks.json"))
    tasks = [
        {"id": 1, "title": "Keep", "status": "pending"},
        {"id": 2, "title": "Delete me", "status": "pending"}
    ]
    result = storage.delete_task(tasks, 2)
    assert len(result) == 1
    assert result[0]["id"] == 1

def test_delete_task_nonexistent(tmp_path, monkeypatch):
    """delete_task with invalid ID should return unchanged list."""
    monkeypatch.setattr(storage, "STORAGE_FILE", str(tmp_path / "tasks.json"))
    tasks = [{"id": 1, "title": "Task", "status": "pending"}]
    result = storage.delete_task(tasks, 99)
    assert len(result) == 1
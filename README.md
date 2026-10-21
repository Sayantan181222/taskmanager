# Task Manager

A command-line task management application built by a team of three
to learn professional Git and GitHub workflow.

## Team

| Name | Role | Branch |
|------|------|--------|
| Sayantan (Sayan) | Task model + core logic | feature/add-task |
| Satyam | Display + listing | feature/list-tasks |
| Anant | Storage + JSON persistence | feature/delete-task |

## Project Structure

taskmanager/
├── main.py        # Entry point
├── tasks.py       # Task data model (Sayan)
├── display.py     # Display logic (Satyam)
├── storage.py     # File I/O (Anant)
└── data/
    └── tasks.json # Task storage

## Setup

    git clone git@github.com:USERNAME/taskmanager.git
    cd taskmanager
    python main.py

## Workflow

We follow GitHub Flow: feature branches → pull requests → code review → merge to main.

![CI](https://github.com/Sayantan181222/taskmanager/actions/workflows/ci.yml/badge.svg)
## Run with Docker

Build the image and run the app without installing Python locally:

```bash
docker compose build
docker compose run --rm app add "Buy groceries"
docker compose run --rm app list
```

Tasks are stored in a named volume (`task-data`), so they persist between runs.
To delete the stored tasks, run `docker compose down -v`.

# Task Manager

A command-line task management application built by a team of three
to learn professional Git and GitHub workflow.

## Team

| Name | Role | Branch |
|------|------|--------|
| Sayantan (Sayan) | Task model + core logic | feature/add-task |
| Satyem | Display + listing | feature/list-tasks |
| Anant | Storage + JSON persistence | feature/delete-task |

## Project Structure

taskmanager/
├── main.py        # Entry point
├── tasks.py       # Task data model (Sayan)
├── display.py     # Display logic (Satyem)
├── storage.py     # File I/O (Anant)
└── data/
    └── tasks.json # Task storage

## Setup

    git clone git@github.com:USERNAME/taskmanager.git
    cd taskmanager
    python main.py

## Workflow

We follow GitHub Flow: feature branches → pull requests → code review → merge to main.
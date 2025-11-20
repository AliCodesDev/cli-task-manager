# Task Manager CLI

A small Python CLI task manager. Defines a `Task` model and `TaskManager` with add/list/complete/delete operations, persists tasks to a JSON file, and routes commands via `sys.argv` so you can manage a simple to‑do list from the terminal.

## Project structure

- tasks/models.py — Task model with mark-complete and (de)serialization.
- tasks/manager.py — Manages a list of Task objects, JSON save/load.
- tasks/main.py — CLI entry point (uses sys.argv).
- tasks/data.json — Saved tasks (ignored by git).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install --upgrade pip
```

## Usage

From tasks/:

```bash
python main.py add "Title" "Description"
python main.py list
python main.py complete 0
python main.py delete 0
```

- Indices are zero-based (see them in the list output).
- Tasks persist in tasks/data.json; first run will create the file.

## Notes

- Unknown commands or missing arguments print a usage hint.
- Add optional fields (created_at, priority, filters) if you extend the exercises.

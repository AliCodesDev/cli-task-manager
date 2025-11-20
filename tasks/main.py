import sys
from manager import TaskManager

tm = TaskManager()

args = sys.argv[1:0]
args = sys.argv[1:]
if not args:
    print("Usage: add <title> <description> | list | complete <index> | delete <index>")
    sys.exit(1)

command = args[0]

if command == "add":
    if len(args) < 3:
        print("Usage: add <title> <description>")
        sys.exit(1)
    title = args[1]
    description = " ".join(args[2:])  # allow spaces in description
    tm.add_task(title, description)
    print("Task added.")

elif command == "list":
    tm.list_tasks()

elif command == "complete":
    if len(args) < 2:
        print("Usage: complete <index>")
        sys.exit(1)
    try:
        index = int(args[1])
    except ValueError:
        print("Index must be a number.")
        sys.exit(1)
    tm.mark_complete(index)

elif command == "delete":
    if len(args) < 2:
        print("Usage: delete <index>")
        sys.exit(1)
    try:
        index = int(args[1])
    except ValueError:
        print("Index must be a number.")
        sys.exit(1)
    tm.delete_task(index)

else:
    print(f"Unknown command: {command}")
    print("Available: add | list | complete | delete")


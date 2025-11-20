from models import Task
from pathlib import Path
import json

class TaskManager:
    
    def __init__(self):
        self.list_of_tasks = []
        self.storage_path = Path(__file__).with_name("data.json")
        self.load_from_json()

    def save_to_json(self):
        with open(self.storage_path, "w") as f:
            data = [task.to_dict() for task in self.list_of_tasks]
            json.dump(data, f)
            
    def load_from_json(self):
        try:
            with open(self.storage_path, "r") as f:
                loaded_tasks = json.loads(f.read())
        except FileNotFoundError:
            return 
        else:
            for task in loaded_tasks:
                self.list_of_tasks.append(Task.from_dict(task))

    def add_task(self, title, description):
        task = Task(title, description)
        self.list_of_tasks.append(task)
        self.save_to_json()

    def delete_task(self, index: int):
        if not isinstance(index, int):
            print("Index must be an integer")
            return
        try:
            self.list_of_tasks.pop(index)
        except IndexError:
            print("Index out of range")
        else:
            self.save_to_json()

    def mark_complete(self, index: int):
        if not isinstance(index, int):
            print("Index must be an integer")
            return
        try:
            task = self.list_of_tasks[index]
            task.mark_complete()
        except IndexError:
            print("Index out of range")
        else:
            self.save_to_json()

        
    def list_tasks(self):
        for index, task in enumerate(self.list_of_tasks):
            print(f"{index}: {task}")
        






    



    

    
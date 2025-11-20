import json
from datetime import datetime


class Task:
    def __init__(self, title, description, completed=False) -> None: # Include a timestamp (optional)
        self.title = title
        self.description = description
        self.completed = completed

    def mark_complete(self):
        self.completed = True
    
    def to_dict(self):
        task_dict = {
            "title" : self.title,
            "description" : self.description,
            "completed" : self.completed
        }
        return task_dict

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            description=data["description"],
            completed=data.get("completed", False),
        )
        

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.title}, {self.description}, {self.completed})"
    
    def __str__(self):
        return f"{self.title} -- {self.description}"
    




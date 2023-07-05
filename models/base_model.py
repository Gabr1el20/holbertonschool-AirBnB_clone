#!/usr/bin/python3
"shebang"

from datetime import datetime
from uuid import uuid4


class BaseModel:
    "class base"

    def __init__(self):
        "instantation"

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        "string replication"
        return (
            f"[BaseModel] ({self.id}) ({self.created_at}) {self.__dict__}"
        )

    def save(self):
        "save function"

        self.updated_at = datetime.now()

    def to_dict(self):
        "return dict"
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict

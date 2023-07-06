#!/usr/bin/python3
"Placeholder"
import json
import os
from models.base_model import BaseModel


class FileStorage():
    "Placeholder"

    __file_path = "file.json"
    __objects = {}

    def all(self):
        "Returns the dictionary '__objects'"
        return FileStorage.__objects

    def new(self, obj):
        "Sets in __objects the object with key <obj class name>.id"
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        "Serializes __objects to the JSON filepath"
        if FileStorage.__objects is not None:
            dict = {}
            for k, v in FileStorage.items():
                dict[k] = v.to_dict()
            with open(FileStorage.__file_path, 'w') as jsonfile:
                dict.dump(dict, jsonfile)

    def reload(self):
        "Deserializes the JSON file to __objects"
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                new = json.load(file)
            for k, v in new.items():
                init = FileStorage.class_dict[v["__class__"]](**v)
                FileStorage.__objects[k] = init

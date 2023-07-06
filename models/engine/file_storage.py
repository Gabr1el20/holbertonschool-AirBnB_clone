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
            for k, v in FileStorage.__objects.items():
                dict[k] = v.to_dict()
            with open(FileStorage.__file_path, 'w') as jsonfile:
                json.dump(dict, jsonfile)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = BaseModel(**obj_dict)
                    self.__objects[key] = obj
        except Exception:
            pass

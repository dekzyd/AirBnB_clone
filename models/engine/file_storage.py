#!/usr/bin/python3

"Filestorage class model"
import json


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        "returns the dictionary __objects"
        return self.__objects

    def new(self, obj):
        "sets the obj with key <obj class name>.id in __objects dictionary"
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        "serializes __objects and saves them in JSON format"
        with open(self.__file_path, mode='w') as file:
            store = {}
            for key, val in self.__objects.items():
                store[key] = val.to_dict()
            json.dump(store, file)

    def reload(self):
        "deserializes the JSON file to __objects"
        try:
            with open(self.__file_path, mode='r') as file:
                json_obj = json.load(file)
                return json_obj
        except Exception as e:
            pass

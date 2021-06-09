#!/usr/bin/python3
"""
Valid arguments id.

Gives the id of an object.
"""
import json


class Base:
    """
    class Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Contructor method."""
        self.id = id

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to create a string into a file."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to save list of strings into a file."""
        if list_objs is None:
            list_objs = []
        dict_list = []
        for i in list_objs:
            dict_list.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w+") as f:
            f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Method to load a list of strings from a file."""
        if json_string is None or json_string == "":
            empty_list = []
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method to create a element from a dummy object."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method to load from a json file."""
        try:
            new_list = []
            with open(cls.__name__ + ".json", "r") as f:
                json_list = cls.from_json_string(f.read())
                for i in json_list:
                    new_list.append(cls.create(**i))
        except:
            return []
        return new_list

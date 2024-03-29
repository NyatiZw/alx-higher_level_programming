#!/usr/bin/python3
""" Define class model base """
import json


class Base:
    """ First class named Base
    Attribute:
        __nb_objects: number of bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Function to initialize a base
        Args:
            id: id element
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        fp = cls.__name__ + ".json"
        with open(fp, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            n = cls(1, 1)
        else:
            n = cls(1)
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                l_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**x) for x in l_dictionaries]
        except IOError:
            return []

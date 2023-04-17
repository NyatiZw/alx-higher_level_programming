#!/usr/bin/python3
class Base:
    __nb_objects = 0


    def __init__(self, id=None):
        self.id = id

    if id is not None:
        id = id
    else:
        __nb_objects += 1
        id = __nb_objects

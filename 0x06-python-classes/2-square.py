#!/usr/bin/python3
class Square:
    size = 0

def __init__(self, size=0):

    self.size = size
    print("{}".format(self.size))
    Square.size += 1

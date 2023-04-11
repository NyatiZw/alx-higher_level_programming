#!/usr/bin/python3
"""

Class MyList that inherits from list
"""

class list(object):
    def __init__(self, list):
        self.list = list

class MyList(list):
    def __init__(self, list):
        self.list = list

        MyList.__init__(self, list)


def print_sorted(self):
    print(MyList.sort())

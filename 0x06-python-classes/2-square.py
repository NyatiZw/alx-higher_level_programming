#!/usr/bin/python3
class Square():

    def __init__(self, size=0):

        try:
            self.size = size
            print("{}".format(self.size))
        except:
            if size < 0:
                raise ValueError:
                    print("size must be >= 0")
            elif size.isdigit(size):
                raise TypeError:
                    print("size must be an integer")

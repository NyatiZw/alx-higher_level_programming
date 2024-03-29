#!/usr/bin/python3
""" Class rectangle that inherits from base """
from models.base import Base


class Rectangle(Base):
    """ Intestates a new class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the rectangle class
        Args:
            width (int): width element of rectangle
            height (int): height element of rectangle
            x (int): integer value
            y (int): integer value
            id (int): Rectangle id
        Raises:
            TypeError: If width or height is not integer
            ValueError: if width or height is less than or equal to zero
            TypeError: if x or y is not an integer
            ValueError: if x or y is less than zero
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Set/get the width """
        return self.__width

    @width.setter
    def width(self, val):
        """ width setter """
        if type(val) != int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """ Set/get the height """
        return self.__height

    @height.setter
    def height(self, val):
        """ height setter """
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        """ Set/get the x element """
        return self.__x

    @x.setter
    def x(self, val):
        """ x setter """
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        """ Set/get the y element """
        return self.__y

    @y.setter
    def y(self, val):
        """ y setter """
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        """ Calculates rectangle area """
        return self.width * self.height

    def display(self):
        """ prints rectangle of # """
        i = 0
        while i < self.height:
            j = 0
            while j < self.width:
                if i == 0 or i == self.height-1 or j == 0 or j == self.width-1:
                    print("#", end="")
                else:
                    print(" ", end="")
                    j += 1
            print()
            i += 1

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ update method
        Attributes:
            id: rectangle id
            width: width size
            heigth: height size
            x: element
            y: element
        """
        if args is not None and len(args) is not 0:
            _list = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, _list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary """
        return {"id": self.id,
                "width": self.width,
                "y": self.y,
                "height": self.height,
                "x": self.x
                }

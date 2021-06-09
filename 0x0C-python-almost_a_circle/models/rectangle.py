#!/usr/bin/python3
"""
Valid arguments width, height, x, y, id.

creates a rectangle and place it with x and y axis.
"""
from models.base import Base


class Rectangle(Base):
    """
    Subclass Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Contructor method."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method to get the area"""
        return self.__width * self.__height

    def display(self):
        """Method to show the representacion of the rectangle"""
        pixel = ""
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            if i < self.__height - 1:
                pixel += " " * self.__x
                pixel += "#" * self.__width
                pixel += "\n"
            else:
                pixel += " " * self.__x
                pixel += "#" * self.__width
        print(pixel)

    def __str__(self):
        """Method that return the information"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Method that update the values with new ones"""
        if args and not None:
            new_order = ["id", "width", "height", "x", "y"]
            for position in range(len(args)):
                setattr(self, new_order[position], args[position])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method to get the directory from an object"""
        new_dict = {}
        for key in self.__dict__:
            new_key = key.replace("_Rectangle__", "")
            new_dict[new_key] = self.__dict__[key]
        return new_dict

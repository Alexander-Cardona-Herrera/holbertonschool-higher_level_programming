#!/usr/bin/python3
"""
Valid arguments size, x, y, id.

creates a rectangle and place it with x and y axis.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Subclass Square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Contructor method."""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Getter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """Method that return the information"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Method that update the values with new ones"""
        if args and not None:
            new_order = ["id", "size", "x", "y"]
            for position in range(len(args)):
                setattr(self, new_order[position], args[position])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method to get the directory from an object"""
        new_dict = {
            "id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return new_dict

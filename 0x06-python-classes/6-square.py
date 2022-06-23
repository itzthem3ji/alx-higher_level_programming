#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square class with a private attribute -
    size.

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size variable as a private
        instance artribute

        """
        self.size = size
        self.position = position

    def area(self):
        """Returns the current square area"""
        return (self.__size) ** 2

    @property
    def size(self):
        """Instantiation with optional size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Gets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Prints the square with the '#' character."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """must be a tuple of 2 positive integers,
        otherwise raise a TypeError exception

        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

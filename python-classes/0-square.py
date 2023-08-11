#!/usr/bin/python3
"""
This module defines the Square class, which represents a square shape.

Square:
    A class to create and manipulate square objects.

"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square instance
        with a given size (default is 0).
        area(self): Calculate and return the area of the square.
        my_print(self): Print the square pattern using '#'.
    """

    def __init__(self, size):
        """
        Constructor for Square class.

        Args:
            __size (int): The size of the square (default is 0).
        """
        self.__size = size
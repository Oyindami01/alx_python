#!/usr/bin/python3
"""
This module defines the Base class which serves as the
foundation for other classes in our project
"""


class Base:
    """
    The Base class will manage the id attribute for
    our other classes in the project
    """
    #private class attribute to keep track of created objects
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of Base class

        Args:
            id(int, optional): An integer representing the id. If
            provided, assigns this value to the instance attribute
            if. If not, it increments __nb_objects attribute and
            assigns the new value to the instance id.

        Attributes:
            id(int): An integer representing the id of the instance.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
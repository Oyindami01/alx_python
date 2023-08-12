#!/usr/bin/python3

"""
This module defines a function to check if object is exactly an instance of a specified class.

Function:
    is_same_class(obj, a_class): Checks if object is exactly an instance of the specified class.

"""

class BaseGeometry:
    """
    This is an empty class representing the base geometry.

    It can be used as a base class to create other geometry-related classes.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
    """
    def __dir__(self):
        """ Get the list of attributes from the parent class (object class)"""
        attributes = super().__dir__()

        """ Exclude __init_subclass__ from the list of attributes"""
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        This method needs to be implemented in the subclass to calculate the
        area of the specific geometry.
        """
        raise Exception("area() is not implemented")
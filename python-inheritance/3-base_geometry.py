#!/usr/bin/python3

"""
This module defines a function to check if an object is exactly an instance of a specified class.

Function:
    is_same_class(obj, a_class): Checks if an object is exactly an instance of the specified class.
"""

class BaseGeometry:
    """
    This is an empty class representing our base geometry.

    It can be used as a base class to create other geometry-related classes.

    Attributes:
        None

    Methods:
        None
    """
    def __dir__(self):
        """
        Get the list of attributes from the parent class (object class),
        excluding '__init_subclass__'.
        """
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

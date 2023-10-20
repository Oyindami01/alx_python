#!/usr/bin/python3

"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

class BaseGeometry:
    """
    This is a base class for geometry-related classes.

    Attributes:
        None

    Methods:
        integer_validator(self, name, value): Validates an integer value.
    """

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Parameters:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    This class represents a Rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with width and height.

        Parameters:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).

        Raises:
            ValueError: If width or height is less than or equal to 0.
        """
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height <= 0:
            raise ValueError("height must be greater than 0")

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

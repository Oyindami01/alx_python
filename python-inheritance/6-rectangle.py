#!/usr/bin/python3

"""
This module defines the BaseGeometry and Rectangle classes.
"""

class BaseGeometry:
    """
    This class represents the base geometry.

    It can be used as a base class to create other geometry-related classes.
    """

    def __dir__(self):
        """
        Get the list of attributes from the parent class (object class)
        """
        attributes = super().__dir()

        """ Exclude __init_subclass__ from the list of attributes
        """
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        This method needs to be implemented in the subclass to calculate
        the area of the specific geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer and raises exceptions if invalid.

        Parameters:
            name (str): The name of the value to be validated.
            value: The value to be validated.

        Raises:
            TypeError, if the value is not an integer.
            ValueError, if the value is <= 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    This class represents a Rectangle.

    It inherits from the BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError, if width or height is not an integer.
            ValueError, if width or height is <= 0.
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

if __name__ == "__main__":
    r = Rectangle(1, 4)
    print(dir(r))
    print(issubclass(Rectangle, BaseGeometry))

    try:
        r = Rectangle(0, 4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(3, "3")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    r = Rectangle(3, 5)
    print(r.__dict__['_Rectangle__width'])

    r = Rectangle(3, 5)
    print(r.__dict__['_Rectangle__height'])

    r = Rectangle()

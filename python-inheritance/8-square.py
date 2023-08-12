#!/usr/bin/python3

"""
This module defines a function to check if object is
exactly an instance of a specified class.

Function:
    is_same_class(obj, a_class): Checks if object is
    exactly an instance of the specified class.

"""


class BaseGeometry:
    """
    This is a class representing the base geometry.

    It can be used as a base class to create other geometry-related classes.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message
        "area() is not implemented".
        integer_validator(self, name, value): Validates the
        value as an integer and raises exceptions if invalid.
    """

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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class represents a Rectangle.

    It inherits from the BaseGeometry class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError when width or height is not an integer.
            ValueError wheh width or height is <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height 
    def get_width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    def get_height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: The rectangle description in the format
            [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def __dir__(self):
        """
        Customizes the list of attributes and methods returned by the dir() function.

        This method overrides the default dir() behavior to exclude the '__init_subclass__'
        attribute from the list.

        Returns:
            list: The list of attributes and methods of the Rectangle class (excluding '__init_subclass__').
        """
       
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']


class Square(Rectangle):
    """
    This class represents a Square.

    It inherits from the Rectangle class.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize the Square with size.

        Parameters:
            size (int): The size of the square.

        Raises:
            TypeError when size is not an integer.
            ValueError when size is <=.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def get_size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: The square description in the format
            [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
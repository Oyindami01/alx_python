#!/usr/bin/python3

class BaseGeometry:
    """
    Base class for geometric operations.

    Methods:
        __dir__(self): Get a list of attributes excluding '__init_subclass__'.
        area(self): Raise an Exception with the message "area() is not implemented".
        integer_validator(self, name, value): Validate an integer and raise exceptions if invalid.
    """

    def __dir__(self):
        """
        Get the list of attributes, excluding '__init_subclass__'.
        """
        attributes = super().__dir()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

    def area(self):
        """
        Raise an Exception with the message "area() is not implemented".

        This method needs to be implemented in the subclass to calculate
        the area of the specific geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer and raise exceptions if invalid.

        Parameters:
            name (str): The name of the value to be validated.
            value: The value to be validated.

        Raises:
            TypeError, if the value is not an integer.
            ValueError, if the value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initialize the Rectangle with width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle with width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is not greater than 0.
        """
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height <= 0:
            raise ValueError("height must be greater than 0")

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

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

#!/usr/bin/python3
"""
This module defines the Square class that inherits from the Rectangle class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class and represents a square shape.
    
    Attributes:
        size (int): The size (width and height) of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): An integer representing the id of the instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size (width and height) of the square.
            x (int, optional): The x-coordinate of the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the square's position. Defaults to 0.
            id (int, optional): An integer representing the id. If provided, assigns this value
                               to the instance attribute id. If not provided, increments the
                               __nb_objects attribute and assigns the new value to the instance id.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        int: The size (width and height) of the square.
        """
        return self.width  # Both width and height are the same for a square

    @size.setter
    def size(self, value):
        """
        Set the size (width and height) of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError, if value is not integer.
            ValueError, if value is not greater than 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
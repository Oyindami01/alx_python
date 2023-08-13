#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from the Base class.
"""


from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class inherits from the Base class
    and represents a rectangle shape.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of rectangle class.

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): An integer representing the id. If provided, assigns this value
                               to the instance attribute id. If not provided, increments the
                               __nb_objects attribute and assigns the new value to the instance id.

        Attrributes:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): An integer representing the id of the instance.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        int: The width of the rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value(int): The new width value.
        
        Raises:
            TypeError, if value is not an integer
            ValueError, if value is not greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError, if value is not an integer.
            ValueError, if value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle's position.

        Args:
            value (int): The new x-coordinate value.

        Raises:
            TypeError, if value is not an integer.
            ValueError, if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle's position.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            TypeError, if value is not an integer.
            ValueError, if value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and returns the area of the rectangle.

        Returns:
        int: The area vslue of the rectangle.
        """
        return self.width * self.height
    
    def display(self):
        """
        Display the rectangle using '#' characters in stdout,
        accounting for x and y offsets.
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    def __str__(self):
        """
        Returns a s tring representation of the rectangle.

        Returns:
         str: A string in the format [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
          Update the attributes of the rectangle using the provided arguments.

        Args:
            *args: Arguments in the order: id, width, height, x, y.
            **kwargs: Key-worded arguments to update the attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value) 
                  
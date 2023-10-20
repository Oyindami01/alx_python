#!/usr/bin/python3

class BaseGeometry:
    def __dir__(self):
        attributes = super().__dir()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    def __init__(self, width=0, height=0):
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height <= 0:
            raise ValueError("height must be greater than 0")

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

if __name__ == "__main":
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

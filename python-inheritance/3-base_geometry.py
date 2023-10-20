#!/usr/bin/python3

class BaseGeometry:
    def __dir__(self):
        # Get the list of attributes from the parent class (object class)
        attributes = super().__dir()

        # Exclude '__init_subclass__' from the list of attributes
        attributes = [attr for attr in attributes if attr != '__init_subclass__']

        return attributes


geometry = BaseGeometry()
print(dir(geometry))

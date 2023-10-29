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
        Get the list of attributes from the parent class (object class).
        """
        attributes = super().__dir__()

       
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

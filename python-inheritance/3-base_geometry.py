class BaseGeometry:
    def __dir__(self):
        # Get the list of attributes from the parent class (object class)
        attributes = super().__dir()

        # Exclude the '__init_subclass__' attribute from the list of attributes
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

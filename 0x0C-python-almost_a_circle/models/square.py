#!/usr/bin/python3

"""class Square that inherites from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherites from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor of square
        Attributes:
            size: int
            x: int, 0 by default
            y: int, 0 by default
            id, int, None by default
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ method for size value
        Return:
            size value: integer greater than 0
        """
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size
        Attribute:
            size value: must be an integer greater than zero
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def __str__(self):
        """method to override the __str__ method
        Returns:
            string: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        x = self.x
        y = self.y
        s = self.size
        return "[Square] ({}) {}/{} - {}".format(self.id, x, y, s)

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each at
        Attributes:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        """
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            attribute_list = ['id', 'size', 'x', 'y']
            for arg, value in enumerate(args):
                setattr(self, attribute_list[arg], value)

    def to_dictionary(self):
        """public method that returns the dictionary representation
        of a Square
        """
        return({"id": self.id, "size": self.size, "x": self.x, "y": self.y})

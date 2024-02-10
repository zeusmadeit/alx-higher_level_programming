#!/usr/bin/python3
"""moudle for Class Square that inherits from Rectangle"""
from rectangle import Rectangle

class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """override the __str__ method so that it returns 
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """the public method update, assigns attributes"""
        if args is not None and len(args) > 0:
            for key, num in enumerate(args):
                self.id = num if key == 0 else self.id
                self.size = num if key == 1 else self.size
                self.x = num if key == 2 else self.x
                self.y = num if key == 3 else self.y
        
        if args is None or len(args) <= 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        attrs = {k.replace("_Rectangle__", ""): getattr(self, k) for k in self.__dict__ if hasattr(self, k)}
        return attrs

if __name__ == "__main__":

    r1 = Square(10, 2, 8)
    print(r1.to_dictionary())
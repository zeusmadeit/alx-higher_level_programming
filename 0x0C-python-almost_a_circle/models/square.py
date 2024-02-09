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


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")
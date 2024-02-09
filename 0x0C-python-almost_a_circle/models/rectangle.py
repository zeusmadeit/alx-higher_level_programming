#!/usr/bin/python3
"""moudle for Class Rectangle that inherits from Base"""
from base import Base

class Rectangle(Base):
    """Rectangle Class Which inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    # List of getter functions
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y
    
    # List of setter functions

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """Returns the area value of the Rectangle Instance"""
        return self.height * self.width
    
    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y in range(self.y):
            print("")
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()
    
    def __str__(self):
        """override the __str__ method 
        so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:"""
        if args is not None and len(args) >= 1:
            for index, n in enumerate(args):
                self.id = n if index == 0 else self.id
                self.width = n if index == 1 else self.width
                self.height = n if index == 2 else self.height
                self.x = n if index == 3 else self.x
                self.y = n if index == 4 else self.y
        elif args is None or len(args) < 1:
            for key, val in kwargs.items():
                setattr(self, key, val)

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

    r1.update(90, 7, 3, 5, x=1, height=2, y=9, width=4)
    print(r1)

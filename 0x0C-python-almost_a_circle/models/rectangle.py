#!/usr/bin/python3
"""moudle for Class Rectangle that inherits from Base"""
from models.base import Base

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
    
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        attrs = {k.replace("_Rectangle__", ""): getattr(self, k) for k in self.__dict__ }
        return attrs

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file_csv()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))


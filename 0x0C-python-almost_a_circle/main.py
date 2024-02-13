"""Main entry module for the program"""
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(80, 110, 60, 60), Rectangle(90, 110, 30, 10), Rectangle(45, 55, 150, 70), Rectangle(80, 45, 100, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Rectangle.save_to_file(list_rectangles)
    print("----\n")
    t = Rectangle.load_from_file()
    for r in t:
        print(r.__str__())
    
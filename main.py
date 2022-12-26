from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import cowsay


def main():
    print(Rectangle.Count_rect)
    r = Rectangle("синего", 3, 2)
    print(Rectangle.Count_rect)
    r1 = Rectangle("синего", 3, 2)
    print(Rectangle.Count_rect)
    r2 = Rectangle("синего", 3, 2)
    print(Rectangle.Count_rect)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)
    cowsay.cow("hello")
    print(cowsay.get_output_string('trex', 'Hello Worrrrrld'))
    print(Rectangle.Count_rect)


if __name__ == "__main__":
    main()

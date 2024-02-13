import unittest
from models.base import Base, Rectangle, Square


class TestBase(unittest.TestCase):
    def test_base_init(self):
        b = Base()
        self.assertIsInstance(b, Base)

    # Add more test cases for Base class methods


class TestRectangle(unittest.TestCase):
    def test_rectangle_init(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r, Rectangle)

    # Add more test cases for Rectangle class methods


class TestSquare(unittest.TestCase):
    def test_square_init(self):
        s = Square(1, 2, 3, 4)
        self.assertIsInstance(s, Square)

    # Add more test cases for Square class methods


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
class
"""

class Rectangle:
    """
    class rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        @property
        def width(self):
            return self.__width
        @property
        def height(self):
            return self.__height
        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

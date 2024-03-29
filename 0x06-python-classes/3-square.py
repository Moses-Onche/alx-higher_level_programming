#!/usr/bin/python3
class Square:
    def __init__(self, size):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        size = self.__size
        return size * size

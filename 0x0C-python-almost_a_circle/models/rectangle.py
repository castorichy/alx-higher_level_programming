from .base import Base

''' Module: Rectangle
its defines a rengle re;ated classes and artributes'''

class Rectangle(Base):
    '''
    Class: Rectangle
defines a rectangle class
it inherits Base class from base module'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        methord: __init__
it accepts arguments and assines to its artribute.
    args:
        width (int, float): width of a rectangle
        height (int, float): heighy of a rectangle
        x (int, float): x of a rectang
    le
        y (int): y of a rectang
    le
        id (int): id of a rectang
    le
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
        super().__init__(id)

    @property
    def get_width(self):
        return self.__width
    @get_width.setter
    def set_width(self, width):
        self.__width = width

    @property
    def get_height(self):
        return self.__height
    @get_height.setter
    def set_height(self, height):
        self.__height = height

    @property
    def get_x(self):
        return self.__x
    @get_x.setter
    def set_x(self, x):
        self.__x = x

    @property
    def get_y(self):
        return self.__y
    @get_y.setter
    def set_width(self, y):
        self.__y = y

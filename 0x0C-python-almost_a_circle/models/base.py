#!/usr/bin/python3
#base defines the base of all clas


'''
    module: Base

Define Base instances
'''
class Base:
    '''
    class: Base

Define Base instances
'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        __init__ methord that creats id
    args:
        __nb_object (int): private instance of class base
    id (int): pubplic instance that defines id of an object
    '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

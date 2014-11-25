#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

def argsToTuple(args, kwargs):
    return (args, tuple(kwargs.items()))

class SingletonType(type):
    def __init__(self, *args, **kwargs):
        self.__instances = {}

    def __call__(self, *args, **kwargs):
        argsTuple = argsToTuple(args, kwargs)

        if argsTuple not in self.__instances:
            self.__instances[argsTuple] = type.__call__(self, *args, **kwargs)
        else:
            print('contains')

        return self.__instances[argsTuple]

class Singleton(object, metaclass = SingletonType):
    def __init__(self, *args, **kwargs):
        self.__tuple = argsToTuple(args, kwargs)

    def __str__(self):
        return str(self.__tuple)

if __name__ == '__main__':
    print(Singleton(1, first_name = 'first', last_name = 'last'))
    print(Singleton(1, name = 'second'))
    print(Singleton(1, last_name = 'last', first_name = 'first'))

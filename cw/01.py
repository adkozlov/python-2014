#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"


class ClassBase(type):
    __attributes = {}

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        l = []
        with open(cls.__name__ + ".txt") as file:
            for line in file.readlines():
                t = tuple(line.strip().split(': ', 1))

                l.append(t)

        ClassBase.__attributes[cls] = l

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)

        for attr in ClassBase.__attributes.get(cls):
            setattr(instance, attr[0], attr[1])

        return instance


class A(metaclass=ClassBase):
    pass


if __name__ == '__main__':
    a = A()
    print(a.y)
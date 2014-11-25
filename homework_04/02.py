#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"


class WithFinals(type):
    __methods = {}
    __final_methods = {}
    __decorated_methods = []

    def __init__(cls, *args, **kwargs):
        methods = dict(args[2])
        WithFinals.__methods[cls] = methods

        WithFinals.__final_methods[cls] = {}
        for method in WithFinals.__decorated_methods:
            if method == methods.get(method.__name__):
                WithFinals.__final_methods[cls][method.__name__] = method

        resolved = {}
        for base in cls.mro():
            methods = WithFinals.__methods[base] if base in WithFinals.__methods else base.__dict__.copy()

            if base in WithFinals.__final_methods:
                for name in methods:
                    if name in resolved and name in WithFinals.__final_methods[base]:
                        raise TypeError(
                            'Method \'' + name + '\' of class \'' + base.__name__ + '\' can not be overridden')

            resolved.update(methods)

    @staticmethod
    def final(method):
        WithFinals.__decorated_methods.append(method)

        return method


def final(method):
    return WithFinals.final(method)


class Foo():
    def foo(self):
        print('foo')


class Bar(Foo):
    pass


class Baz(Bar, metaclass=WithFinals):
    @final
    def foo(self):
        print('baz')


class BarBaz(Baz, Bar):
    def foo(self):
        print('bar baz')

# class Bar(metaclass=WithFinals):
#     @final
#     def foo(self):
#         print('bar')
#
#
# class Baz(Foo, Bar):
#     pass

if __name__ == '__main__':
    pass
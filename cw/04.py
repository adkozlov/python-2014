#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"


import functools


class ApplyDecorator:
    __decorated_methods = {}
    __original_methods = {}
    __names = {}

    @staticmethod
    def universal_method(name, *args, **kwargs):
        for (test_func, func) in ApplyDecorator.__decorated_methods[name].items():
            if test_func(*args, **kwargs):
                return ApplyDecorator.__decorated_methods[name][test_func](*args, **kwargs)

        return ApplyDecorator.__original_methods[name](*args, **kwargs)

    @staticmethod
    def apply(func, test_func):
        name = None
        if not isinstance(func, functools.partial):
            name = func.__name__
            ApplyDecorator.__decorated_methods[name] = {}
            ApplyDecorator.__original_methods[name] = func

            result = functools.partial(ApplyDecorator.universal_method, name)
            ApplyDecorator.__names[result] = name

            globals()[name] = result
        else:
            name = ApplyDecorator.__names[func]

        def decorator(f):
            ApplyDecorator.__decorated_methods[name][test_func] = f

            def apply_arguments(*args, **kwargs):
                return ApplyDecorator.universal_method(name, *args, **kwargs)

            return apply_arguments

        return decorator


def apply(func, test_func):
    return ApplyDecorator.apply(func, test_func)


def test1(num):
    return num == 1


def test2(num):
    return num > 3


def foo(num):
    print('Original')


@apply(foo, test1)
def foo2(num):
    print('Modified')


@apply(foo, test2)
def foo3(num):
    print('Magic')


if __name__ == '__main__':
    foo(-1)
    foo(1)
    foo(2)
    foo(4)
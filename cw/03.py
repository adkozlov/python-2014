#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

import datetime


class Spy:
    __times = {}
    __names = {}

    @staticmethod
    def add_time(func):
        def add_pair(*args, **kwargs):
            now = (datetime.datetime.now(), args, kwargs)

            if func in Spy.__times:
                Spy.__times[func].append(now)
            else:
                Spy.__times[func] = [now]

            return func(*args, **kwargs)

        Spy.__names[add_pair] = func
        return add_pair

    @staticmethod
    def get_times(func):
        return Spy.__times[Spy.__names[func]]


def spy(func):
    return Spy.add_time(func)


def bond(func):
    yield from Spy.get_times(func)


@spy
def print_hello(arg):
    print('hello %s' % arg)


@spy
def print_hello2(arg):
    print('hello2 %s' % arg)

if __name__ == '__main__':
    print_hello(1)
    print_hello(2)

    print_hello2(3)

    for time in bond(print_hello):
        print(time)
    for time in bond(print_hello2):
        print(time)
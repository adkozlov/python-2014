#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

import collections
import itertools
import random


class Shuffle:
    def __init__(self, it, n=0):
        try:
            self.__it_len = len(it)
        except TypeError as e:
            self.__it_len = e

        self.__it = iter(it)

        self.__deque = collections.deque(maxlen=n + 1)
        for _ in range(self.__deque.maxlen):
            self.__deque.append(None)

        self.__is_iterated = False

        self.__prev_list = collections.deque()
        self.__next_list = collections.deque()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__next_list) != 0:
            result = self.__next_list.popleft()
            self.__prev_list.append(result)

            return result

        if self.__is_iterated:
            return self.__cache_and_return(next(self.__deque))

        try:
            while self.__deque[0] is None:
                self.__deque[self.__empty_cell_index()] = next(self.__it)
        except StopIteration:
            self.__is_iterated = True
            self.__deque = iter(filter(None.__ne__, self.__deque))

            return self.__cache_and_return(next(self.__deque))

        if not self.__deque[0] is None:
            result = self.__deque.popleft()
            self.__deque.append(None)

            return self.__cache_and_return(result)

    def __prev__(self):
        if len(self.__prev_list) != 0:
            result = self.__prev_list.pop()
            self.__next_list.appendleft(result)

            return result

    def __cache_and_return(self, value):
        self.__prev_list.append(value)
        return value

    def __random_cell_index(self):
        return random.randint(0, self.__deque.maxlen - 1)

    def __empty_cell_index(self):
        result = self.__random_cell_index()
        while not self.__deque[result] is None:
            result = self.__random_cell_index()

        return result

    def __len__(self):
        if isinstance(self.__it_len, TypeError):
            raise self.__it_len
        else:
            return self.__it_len

    def __str__(self):
        if isinstance(self.__it_len, TypeError):
            return super().__str__()
        else:
            return str(list(self))


class Fib:
    def __init__(self):
        self.__fst = 1
        self.__snd = 1

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.__snd
        self.__snd += self.__fst
        self.__fst = temp

        return temp


if __name__ == '__main__':
    length = 10
    n = 3

    lst = [i for i in range(length)]
    shf_it = Shuffle(lst, n)

    result = True
    for (i, x) in enumerate(shf_it):
        if not i in range(x - n, x + n + 1):
            result = False

    print(result)
    print(len(lst) == len(shf_it))

    shf_it = Shuffle(Fib(), 4)
    print(shf_it)
    print(next(shf_it))
    print(next(shf_it))
    print(shf_it.__prev__())
    print(shf_it.__prev__())
    print(next(shf_it))
    print(next(shf_it))
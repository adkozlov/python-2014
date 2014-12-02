#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left

        yield self.value

        if self.right:
            yield from self.right


class Tree:
    def __init__(self):
        self.__root = None

    def __add__(self, arg):
        if isinstance(arg, Tree):
            for value in arg:
                self += value

            return self

        if isinstance(arg, int) or isinstance(arg, float):
            if self.__root:
                Tree.__add_to(self.__root, arg)
            else:
                self.__root = Node(arg)

            return self

        raise ValueError('illegal type')

    @staticmethod
    def __add_to(node, value):
        if value < node.value:
            if node.left:
                Tree.__add_to(node.left, value)
            else:
                child = Node(value)
                node.left = child
        else:
            if node.right:
                Tree.__add_to(node.right, value)
            else:
                child = Node(value)
                node.right = child

    def __iter__(self):
        yield from self.__root


import random

if __name__ == '__main__':
    tree = Tree()

    for i in range(100):
        tree = tree + random.randint(0, 100)

    for i in tree:
        print(i)
#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

from collections import OrderedDict


class InstancesRegistry:
    __instances = OrderedDict()

    @staticmethod
    def register(cls):
        InstancesRegistry.__instances[cls] = 0
        cls.__init__ = InstancesRegistry.__new_init(cls, cls.__init__)

        return cls

    @staticmethod
    def __new_init(cls, init_func):
        def new_init_fun(this):
            old_counts = InstancesRegistry.__instances.copy()

            init_func(this)
            InstancesRegistry.__inc_count(cls)

            for base in cls.__bases__:
                InstancesRegistry.__recursive_inc_count(base, old_counts)

        return new_init_fun

    @staticmethod
    def __inc_count(cls, value=None):
        if cls in InstancesRegistry.__instances:
            if (not value is None) and InstancesRegistry.__instances[cls] != value:
                return

            InstancesRegistry.__instances[cls] += 1

    @staticmethod
    def __recursive_inc_count(cls, old_counts, bases=set()):
        if cls == object or cls in bases:
            return

        InstancesRegistry.__inc_count(cls, old_counts.get(cls))

        for base in cls.__bases__:
            InstancesRegistry.__recursive_inc_count(base, old_counts, bases)

    @staticmethod
    def print_counts():
        for (cls, value) in InstancesRegistry.__instances.items():
            print('%s: %d' % (cls.__name__, value))


def register(cls):
    return InstancesRegistry.register(cls)


@register
class A:
    pass


class B(A):
    pass


@register
class C:
    pass


class D(C):
    pass


@register
class E(B, D):
    pass


if __name__ == '__main__':
    E()

    InstancesRegistry.print_counts()
#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

def insert(it, n):
	try:
		i = next(it)

		while i < n:
			yield i
			i = next(it)
	except StopIteration:
		yield n
	
	try:
		yield n
		yield i

		yield from it
	except StopIteration:
		return

import itertools

def insertion_sort(it):
	fst, snd = itertools.tee(it)
	for i in fst:
		insert(snd, i)

	return snd

if __name__ == '__main__':
	l = [8, 4, 6, 7, 8]
	for i in insertion_sort(iter(l)):
		print(i)
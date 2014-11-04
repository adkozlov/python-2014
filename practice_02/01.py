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

if __name__ == '__main__':
	l = [4, 5, 7, 8]
	for i in insert(iter(l), 6):
		print(i)
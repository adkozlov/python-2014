#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

import itertools
import random

def merge_generator(it1, it2):
	i = None
	j = None

	try:
		i = next(it1)
	except StopIteration:
		while True:
			yield from it2
		return

	try:
		j = next(it2)
	except StopIteration:
		while True:
			yield from it1
		return

	while True:
		if (i < j):
			yield i
			try:
				i = next(it1)
			except StopIteration:
				i = None
				break
		else:
			yield j
			try:
				j = next(it2)
			except StopIteration:
				j = None
				break

	if i == None:
		while True:
			yield j
			j = next(it2)
	else:
		while True:
			yield i
			i = next(it1)

def len(it):
	result = 0
	for _ in it:
		result += 1

	return result

def merge_sort(it):
	fst, snd, trd = itertools.tee(it, 3)
	length = len(iter(trd))
	mid = length // 2

	return merge_generator(merge_sort(itertools.islice(fst, mid)), merge_sort(itertools.islice(snd, mid, None))) if length > 1 else fst

class random_generator:
	def __init__(self, n=100, randmax=100):
		self.n = n
		self.i = 0
		self.randmax = randmax

	def __iter__(self):
		return self

	def __next__(self):
		if self.i == self.n:
			raise StopIteration
		else:
			self.i += 1
			return random.randint(0, self.randmax)

if __name__ == '__main__':
	for i in merge_sort(random_generator()):
		print(i, end=" ")
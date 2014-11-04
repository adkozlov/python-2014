#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

import sys
import itertools

def reverse(x):
	return x[::-1]

def sum_digits(x, y):
	s = int(x) + int(y)
	return (s % 10, s >= 10)

def sum_numbers(x, y):	
	sums = [sum_digits(fst, snd) for (fst, snd) in list(itertools.zip_longest(reverse(x), reverse(y), fillvalue='0'))]

	result = []
	inc = False
	for (x, y) in sums:
		digit = x + 1 if inc else x
		result.append(str(digit % 10))

		inc = y or digit >= 10
	
	if (inc):
		result.append('1')

	return "".join(reverse(result))

if __name__ == '__main__':
	print(sum_numbers(sys.argv[1], sys.argv[2]))
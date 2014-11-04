#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

if __name__ == '__main__':
	n = 5
	for l in ([1 if j in range(n // 2 + 1 - i - 1, n // 2 + 1 + i) else 0 for j in range(n)] for i in range(n)):
		print(l)

#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

def Singleton(cls):
	instance = {}

	def get_instance(*args, **kw):
		if cls not in instance:
			instance[cls] = cls(*args, **kw)

		return instance[cls]

	return get_instance

import time

@Singleton
class timestamp(object):
	def __init__(self):
		self.__time = time.time()

	def __str__(self):
		return str(self.__time)

if __name__ == '__main__':
	print(timestamp())	
	print(timestamp())
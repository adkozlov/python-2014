#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

import time

def get_ms():
	return time.time() * 1000.0

def read_file(path):
	f = open(path, "r")
	result = f.readlines()
	f.close()

	return result

def start_script():
	return '''
start_time = get_ms()
'''

def decorate_file(path):
	content = read_file(path)

	script = start_script()
	for line in content:
		temp = line.lstrip()

		if temp.startswith("def "):
			script += '''
%s@time_decorator_maker
''' % line[0:len(line) - len(temp)]
		
		script += line

	return script

def decorator_lines():
	return '''
import time

def get_ms():
	return time.time() * 1000.0

def time_decorator_maker():
	def time_decorator(func):
		def print_time(*args, **kw):
			start = get_ms()

			print("%.2fms %s" % ((start - start_time), func.__name__))
			
			result = func(*args, **kw)
			finish = get_ms()

			print("+%.2fms" % (finish - start))

			return result

		return print_time

	return time_decorator
'''

import sys

if __name__ == '__main__':
	decorated_file = decorate_file(sys.argv[1])

	exec(decorator_lines())
	exec(decorated_file)
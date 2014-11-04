#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

import sys
import xml.etree.ElementTree as et

def print_element(element, indent):
	print("%s%s" % (indent, element))

def print_with_indent(element, indent, tab):
	print_element(element.tag, indent)
	
	for child in element:
		print_with_indent(child, indent + tab, tab)

	print_element(element.text, indent + tab)
	print_element(element.tag, indent)

def print_rss(argument, tab='\t'):
	print_with_indent(et.parse(argument).getroot(), '', tab)

if __name__ == '__main__':
	print_rss(sys.argv[1], tab='  ')
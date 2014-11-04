#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

class DeniedKeyException(Exception):
	def __init__(self, message):
		super(Exception, self).__init__(self, message)

class extended_dict(dict):
	def __init__(self, denied_keys = [], *args, **kw):
		super(extended_dict, self).__init__(*args, **kw)

		self.__dict__["_denied_keys"] = denied_keys
		self.__dict__["_added"] = []

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			try:
				return self[key.replace('_', ' ')]
			except:
				raise AttributeError("key %s is not in dictionary" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def __getitem__(self, key):
		try:
			return super(extended_dict, self).__getitem__(key)
		except KeyError:
			try:
				return super(extended_dict, self).__getitem__(self._added[key])
			except:
				raise KeyError(str(key))

	def __setitem__(self, key, value):
		if key in self._denied_keys:
			raise DeniedKeyException("key %s is denied" % key)

		super(extended_dict, self).__setitem__(key, value)

		if not key in self._added:
			self._added.append(key)

	def __delitem__(self, key):
		super(extended_dict, self).__delitem__(key)

		self._added.remove(key)

if __name__ == '__main__':
	d = extended_dict(['python'])
	
	d.key_key = 'new value'
	print(d.key_key)

	d.key = 'value'

	print(d[1])
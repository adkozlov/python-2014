#!/usr/bin/env python3

__author__ = "Andrew Kozlov"
__copyright__ = "Copyright 2014, SPbAU"

class vector3(object):
	def __init__(self, vector):
		self.__list = [0.0 for i in range(len(self))]

		for (i, x) in enumerate(vector):			
			self[i] = x

	def __str__(self):
		return ", ".join("%f" % x for x in self)

	def __repr__(self):
		return "vector: %s" % str(self)

	def __len__(self):
		return 3

	def __iter__(self):
		yield from self.__list

	def __getitem__(self, i):
		return self.__list[i]

	def __setitem__(self, i, value):
		if isinstance(value, int) or isinstance(value, float):
			self.__list[i] = float(value)
		else:
			raise Exception("cannot set value %s on index %d" % (str(value), i))

	def __delitem__(self, i):
		raise Exception("cannot remove item from vector")

import itertools
import operator

class matrix3(object):
	def __init__(self, matrix):
		self.__list = [vector3(row) for row in matrix]

	def __str__(self):
		return "\n".join(str(row) for row in self)

	def __repr__(self):
		return '''matrix:
%s
''' % str(self)

	def __len__(self):
		return 3

	def __iter__(self):
		yield from self.__list

	def __getitem__(self, i):
		return self.__list[i]

	def __setitem__(self, i, value):
		if isinstance(value, vector3):
			self.__list[i] = value
		else:
			raise Exception("cannot set %s as row" % type(value))

	def __delitem__(self, i):
		raise Exception("cannot remove row from matrix")

	def __add__(self, other):
		if not isinstance(other, matrix3):
			raise Exception("addition is not defined for %s" % type(other))

		return matrix3([list(map(operator.add, row1, row2)) for (row1, row2) in zip(self, other)])

	def __radd__(self, other):
		return self + other

	def __mul__(self, other):
		if isinstance(other, matrix3):
			return matrix3([[sum(map(operator.mul, self[i], list(zip(*other))[j])) for j in range(len(self))] for i in range(len(self))])
		if isinstance(other, vector3):
			return matrix3([map(operator.mul, row, other) for row in self])
		if isinstance(other, int) or isinstance(other, float):
			return matrix3([map(lambda x: x * other, row) for row in self])

	def __rmul__(self, other):
		if isinstance(other, vector3):
			raise Exception("cannot multiply vector by matrix")
		
		return self * other

	def __invert__(self):
		det = self._det()
		if det == 0:
			raise Exception("cannot inverse matrix")

		result = [[0 for j in range(len(self))] for i in range(len(self))]

		result[0][0] = self[1][1] * self[2][2] - self[2][1] * self[1][2]
		result[1][0] = self[2][0] * self[1][2] - self[1][0] * self[2][2]
		result[2][0] = self[1][0] * self[2][1] - self[2][0] * self[1][1]
		result[0][1] = self[2][1] * self[0][2] - self[0][1] * self[2][2]
		result[1][1] = self[0][0] * self[2][2] - self[2][0] * self[0][2]
		result[2][1] = self[2][0] * self[0][1] - self[0][0] * self[2][1]
		result[0][2] = self[0][1] * self[1][2] - self[1][1] * self[0][2]
		result[1][2] = self[1][0] * self[0][2] - self[0][0] * self[1][2]
		result[2][2] = self[0][0] * self[1][1] - self[1][0] * self[0][1]

		return matrix3(result) * (1 / det)

	def _det(self):
		return   (self[0][0] * (self[1][1] * self[2][2] - self[1][2] * self[2][1])
				- self[0][1] * (self[1][0] * self[2][2] - self[2][0] * self[1][2])
				+ self[0][2] * (self[1][0] * self[2][1] - self[2][0] * self[1][1]))

import math

class z_rotation_matrix(matrix3):
	def __init__(self, angle):
		rad = angle / 180 * math.pi
		super(z_rotation_matrix, self).__init__([[math.cos(rad), -math.sin(rad), 0], [math.sin(rad),  math.cos(rad), 0] ,[0, 0, 1]])

if __name__ == '__main__':
	m = matrix3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	# print(2 * m)
	# print(m * vector3([1, 0, 0]))
	# print(m * m)
	m[2][2] = 10
	print(~m)

	print(z_rotation_matrix(45))
#!/usr/bin/env python3

def multiply_matrices(m1, m2):
	result = []

	if len(m1[0]) != len(m2):
		raise Exception("Illegal arguments")

	for i in range(len(m1)):
		row = []		

		for j in range(len(m2[0])):
			value = 0

			for k in range(len(m2)):
				value += m1[i][k] * m2[k][j]

			row.append(value)

		result.append(row)

	return result

def print_matrix(m):
	for row in m:
		for value in row:
			print("%9d" % value, end="")

		print(end="\n")

m1 = [[1, 0], [1,  1], [0, 1]]
m2 = [[1, 0, 0], [0, 1, 0]]
print_matrix(multiply_matrices(m1, m2))
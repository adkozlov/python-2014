#!/usr/bin/env python3

l = [1, 3, 5, 2]

result = []

i = 0
while i < len(l):
	length = int(l[i])
	result.append(tuple(l[i:i + length]))
	i += length

print(result)
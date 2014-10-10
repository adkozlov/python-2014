#!/usr/bin/env python3

import sys

def generate_primes(n):
	result = [2]
	
	for k in range(2, n):
		if k in result:	
			continue

		is_prime = True
		for p in result:
			if k % p == 0:
				is_prime = False
				break

		if is_prime:
			result.append(k)

	return result

n = int(sys.argv[1])

primes = generate_primes(n // 2)

result = []
for i in range(len(primes)):
	for j in range(i, len(primes)):
		value = primes[i] * primes[j]

		if value < n:
			result.append(value)

print(result)
#!/usr/bin/env python3

import string
import sys

words = []
for raw_line in open(sys.argv[1], "r").readlines():
	line = "".join(c for c in raw_line.rstrip() if c not in string.punctuation)
	words.extend(line.lower().split(" "))

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

nouns = set()
for word in words:
	p = morph.parse(word)[0]

	if 'NOUN' in p.tag:
		nouns.add(p.normal_form)

print(len(nouns))
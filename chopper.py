# To use this program, point it toward a corpus of text and then specifiy a keyword
# to search for and the number of random lines containing that keyword you want it to return. 
# Example: "python chopper.py <rozay.txt chopper 7"

import sys
import re
import random

keyword = sys.argv[1]
lines = int(sys.argv[2])
matching_lines = list()

for line in sys.stdin:
  line = line.strip()
  if re.search(r'\b'+keyword+r'\b', line):
  	if line not in matching_lines:
  		matching_lines.append(line)

random.shuffle(matching_lines)

for x in xrange(0, lines):
	print matching_lines[x]
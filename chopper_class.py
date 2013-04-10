#Same as chopper.py but in class form, for incorporating into other Python scripts.
#If run from the command line, it will provide example output generated from a text file.

class Chopper(object):

	def __init__(self, keyword, n):
		self.n = n
		self.keyword = keyword
		self.matching_lines = list()

	def chop(self, text):
		import re
		for line in text:
	  		line = line.strip()
	  		if re.search(r'\b'+self.keyword+r'\b', line):
	  			if line not in self.matching_lines:
	  				self.matching_lines.append(line)

	def gen(self):
		import random
		random.shuffle(self.matching_lines)
		for x in xrange(0, int(self.n)):
			print self.matching_lines[x]


if __name__ == '__main__':

	import chopper_class 
	text1 = open("rozay.txt") 
	chopper = chopper_class.Chopper(keyword="chopper", n=5)
	chopper.chop(text=text1)
	chopper.gen()














import string
import random


class Alphabet(object):
	def __init__(self, autogen=False, num=0, chars=None):
		self.alph = []
		if autogen == True:
			while len(self.alph) < num:
				# need another function to add element to alphabet
				# for don't add the same elements
				self.alph.append(random.choice(string.letters))
		
		if chars != None:
			self.alph.extend(chars)

	def add(self):
		pass

	def dlt(self):
		pass

	def check_symbol(self, symb):
		if symb in self.alph:
			return True
		return False

	def check_word(self, word):
		for s in word:
			if self.check_symbol(s) == False:
				return False
		return True

	def get(self):
		return "[" + " ".join(self.alph) + "]"


if __name__ == '__main__':
	alp = Alphabet(chars=['a', 'b', 'c'])
	print(alp.get())
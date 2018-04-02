import string
import random


class Alphabet(object):
	def __init__(self, chars=None, autogen=False, num=0):
		self.alph = []
		if chars != None:
			self.alph.extend(chars)
		
		if autogen == True:
			while len(self.alph) < num:
				self.alph.add(radnom.choice(string.letters))

	def get(self):
		return self.alph
		
	def check_symbol(self, symb):
		if symb in self.alph:
			return True
		return False

	def check_word(self, word):
		for s in word:
			if self.check_symbol(s) == False:
				return False
		return True

	def add(self, symb):
		if self.check_symbol(symb) == False:
			self.alph.append(str(symb))
			return True
		return False

	def dlt(self, symb):
		if self.check_symbol(symb) == True:
			self.alph.remove(symb)
			return True
		return False

	def __repr__(self):
		return "[" + " ".join(self.alph) + "]"


if __name__ == '__main__':
	alp = Alphabet(chars=['a', 'b', 'c'])
	print(alp)
	print(alp.get())
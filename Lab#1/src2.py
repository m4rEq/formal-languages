from src1 import Alphabet


class Dictionary(object):
	def __init__(self, alphabet):
		self.alphabet = alphabet
		self.list_of_words = []
		# self.dict_of_words = {}

	def get(self):
		return "[" + ", ".join(self.list_of_words) + "]"

	def search(self, word):
		if word in list_of_words:
			# return dict_of_words[word]
			return word
		return "Not found!"

	def add(self, word): #, mean):
		if word in self.list_of_words:
			msg = "The word already is in dictionary!"
		else:
			if self.alphabet.check_word(word) == True:
				self.list_of_words.append(word)
				msg = "Done!"
			else:
				msg = "Some symbol(s) of word does not match no one symbol from the alphabet!"
		print(msg)

	def dlt(self, word):
		if word in self.list_of_words:
			self.list_of_words.remove(word)
			print("Done!")
		else:
			print("Word {} has no in dictionary!".format(word))

	def sort(self):
		pass


if __name__ == '__main__':
	alp = Alphabet(chars=['a', 'b', 'c'])

	d = Dictionary(alp)
	d.add('abba')
	d.add('acab')
	d.add('alaverdi')
	print(d.get())
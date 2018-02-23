from alphabet import Alphabet


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
				msg = "Some symbol(s) of word \"{}\" does not match no one symbol from the alphabet!".format(word)
		print(msg)

	def dlt(self, word):
		if word in self.list_of_words:
			self.list_of_words.remove(word)
			print("Done!")
		else:
			print("Word {} has no in dictionary!".format(word))

	def dict_sort(self):
		self.list_of_words.sort(key=lambda x: self.alphabet.get().index(x[0]))


if __name__ == '__main__':
	alp = Alphabet(chars=['c', 'b', 'a'])

	d = Dictionary(alp)
	d.add('abba')
	d.add('acab')
	d.add('caba')
	d.add('caca')
	d.add('baba')
	d.add('baca')
	d.add('alaverdi')
	print(d.get())
	d.dict_sort()
	print(d.get())
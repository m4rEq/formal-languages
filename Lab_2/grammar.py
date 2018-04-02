from alphabet import Alphabet
import string


class Grammar(object):
	def __init__(self, l_N, l_E):
		self.rules = dict()
		l1 = l_N
		l2 = l_E
		# l1 = string.ascii_uppercase
		# l2 = string.ascii_lowercase
		check_intersection = list(set(l1) & set(l2))
		if len(check_intersection) == 0:	
			self.N = Alphabet(chars=l1)
			self.E = Alphabet(chars=l2)
		else:
			raise AttributeError("Alphabets mustn't intersection!")
		
		tmp_alph = list(self.N.get())
		tmp_alph.extend(self.E.get())
		self.common_alph = Alphabet(chars=tmp_alph)

	def add_rule(self, rule):
		word, repl = rule.split(" => ")
		self.rules[word] = repl

	def dlt_rule(self, rule):
		word, repl = rule.split(" => ")
		if word in self.rules:
			self.rules[word].remove(repl)

	def action(self, string):
		return string.replace("S", self.rules["S"][0])

	def check_word(self, word):
		return self.common_alph.check_word(word)

	def __repr__(self):
		res_string = ""
		for k, v in self.rules.items():
			res_string += f"{k} => {v}" + "\n"
		return res_string


def main():

	l1 = string.ascii_uppercase
	l2 = string.ascii_lowercase

	gram = Grammar(l1, l2)

	print(gram.rules)
	gram.add_rule("S => abc")
	gram.add_rule("S => bca")
	gram.add_rule("G => ggg")

	print(gram)

	print(gram.check_word("Hello"))
	print(gram.check_word("Hello!"))


if __name__ == '__main__':
	main()


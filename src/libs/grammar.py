from libs.alphabet import Alphabet
import string
import re


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
		print_text = f"Была добавлена {word} => {repl}, Тип = "
		if len(word) > 1:
			print(print_text + "КЗ")
		elif self.N.check_symbol(repl[0]) or self.N.check_symbol(repl[-1]):
			print(print_text + "Грамматика 3его типа")
		else:
			print(print_text + "КС")

	def type_rule(self):
		pass

	def dlt_rule(self, rule):
		word, repl = rule.split(" => ")
		if word in self.rules:
			self.rules[word].remove(repl)

	def action(self, word, rule, num=10):
		#return word.replace(rule, self.rules[rule], num)
		# return string.replace("S", self.rules["S"][0])
		# import re
		res = [m.start() for m in re.finditer(rule, word)]
		print(res)
		if num > len(res): num = len(res)
		res_list = list(word)
		return res_list[res[num-1]]
		# [0, 5, 10, 15]

	def check_word(self, word):
		return self.common_alph.check_word(word)

	def __repr__(self):
		res_string = ""
		for k, v in self.rules.items():
			res_string += f"{k} => {v}" + "\n"
		return res_string



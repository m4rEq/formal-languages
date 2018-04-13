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
		# two alphabet haven't to intersaction
		check_intersection = list(set(l1) & set(l2))
		if len(check_intersection) == 0:	
			self.N = Alphabet(chars=l1)
			self.E = Alphabet(chars=l2)
		else:
			raise AttributeError("Алфавиты не должны пересекаться!")
		# create common alphabet for membership check
		tmp_alph = list(self.N.get())
		tmp_alph.extend(self.E.get())
		self.common_alph = Alphabet(chars=tmp_alph)

	def add_rule(self, rule):
		"""obj.add_rule('A => bc')  new self.rules, print(Type of grammar)"""
		word, repl = rule.split(" => ")
		self.rules[word] = repl
		print_text = f"Была добавлена {word} => {repl}, Тип = "
		if len(word) > 1:
			print(print_text + "КЗ")
		elif self.N.check_symbol(repl[0]) or self.N.check_symbol(repl[-1]):
			print(print_text + "Грамматика 3его типа")
		else:
			print(print_text + "КС")

	def dlt_rule(self, rule):
		"""obj.dlt_rule('A') dlt self.rule """
		if rule in self.rules:
			del rules[rule]
		# If rule have any forms
		#
		# word, repl = rule.split(" => ")
		# if word in self.rules:
		# 	self.rules[word].remove(repl)

	def apply(self, word, rule, index):
		"""obj.apply('Alo', 'A', 0) -> bclo"""
		if self.check_word(word) == False:
			return "Слово не пренадлежит алфавиту!"
		if index > len(word)-1 and index < 0:
			return "Индекс за пределами слова"
		if rule != word[index]:
			return "Неверная попытка замены!"
		return word[0:index] + self.rules[rule] + word[index+1:len(word)]

	### For ordinal case
	###
	# def apply_advanced(self, word, rule, num=10):
	# 	res = [m.start() for m in re.finditer(rule, word)]
	# 	print(res)
	# 	if num > len(res): num = len(res)
	# 	res_list = list(word)
	# 	return res_list[res[num-1]]
	# 	# [0, 5, 10, 15]

	def check_word(self, word):
		"""Is common alphabet include letters of word """
		return self.common_alph.check_word(word)

	def __repr__(self):
		res_string = ""
		for k, v in self.rules.items():
			res_string += f"{k} => {v}" + "\n"
		return res_string



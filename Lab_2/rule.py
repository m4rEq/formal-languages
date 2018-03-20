
class Rule(object):
	def __init__(self):
		self.rules = dict()

	def add_rule(self, rule):
		word, repl = rule.split(" => ")
		if word not in self.rules:
			self.rules[word] = []
		self.rules[word].append(repl)

	def dlt_rule(self, rule):
		word, repl = rule.split(" => ")
		if word in self.rules:
			self.rules[word].remove(repl)

	def action(self, string):
		return string.replace("S", self.rules["S"][0])


obj = Rule()

print(obj.rules)
obj.add_rule("S => abc")
obj.add_rule("S => bca")
obj.add_rule("G => ggg")
print(obj.rules)
obj.dlt_rule("S => bca")
print(obj.rules)
print(obj.action("Salam"))


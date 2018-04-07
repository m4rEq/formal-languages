from libs.grammar import Grammar
import string


def main():
	l1 = string.ascii_uppercase
	l2 = string.ascii_lowercase

	grmr = Grammar(l1, l2)

	grmr.add_rule("S => abc")
	grmr.add_rule("G => ggg")

	print(grmr)

	print(grmr.check_word("Hello"))
	print(grmr.check_word("Hello!"))


if __name__ == '__main__':
	main()

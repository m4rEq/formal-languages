from libs.grammar import Grammar
import string


def main():
	l1 = string.ascii_uppercase
	l2 = string.ascii_lowercase

	grmr = Grammar(l1, l2)

	grmr.add_rule("S => aTbc")
	grmr.add_rule("G => ggg")
	grmr.add_rule("aB => daca")
	grmr.add_rule("T => Aba")

	print(grmr.apply("SaGadaS", "S", 6))




if __name__ == '__main__':
	main()

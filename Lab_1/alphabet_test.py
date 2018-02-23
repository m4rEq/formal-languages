from alphabet import Alphabet
import unittest as ut


class AlphabetTest(ut.TestCase):
	def setUp(self):
		self.apl1 = Alphabet(['b', 'c', 'a'])

	def test_check_symbol(self):
		self.assertEqual(self.apl1.check_symbol('a'), True)
		self.assertEqual(self.apl1.check_symbol('d'), False)

	def test_check_word(self):
		self.assertEqual(self.apl1.check_word('aca'), True)
		self.assertEqual(self.apl1.check_word('bacad'), False)

	def test_get(self):
		self.assertEqual(self.apl1.get(), ['b', 'c', 'a'])

	# def test_get(self):
	# 	# alp = Alphabet(chars=['a', 'b', 'c'])
	# 	self.assertEqual(self.alp1, "[b c a]")

if __name__ == '__main__':
	ut.main()

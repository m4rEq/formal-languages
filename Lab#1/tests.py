from src2 import Dictionary
from src1 import Alphabet
import unittest as ut


class AlphabetTest(ut.TestCase):
	# def setUP(slef):
	# 	self.alp = Alphabet(chars=[a, b, c])
	def setUp(self):
		self.alp = Alphabet(chars=['a', 'b', 'c'])

	def test_get(self):
		# alp = Alphabet(chars=['a', 'b', 'c'])
		self.assertEqual(self.alp.get(), "[a b c]")

if __name__ == '__main__':
	ut.main()

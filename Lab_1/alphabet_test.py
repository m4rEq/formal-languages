from alphabet import Alphabet


class AlphabetTest(ut.TestCase):
	def setUp(self):
		self.alp = Alphabet(chars=['a', 'b', 'c'])

	def test_get(self):
		# alp = Alphabet(chars=['a', 'b', 'c'])
		self.assertEqual(self.alp.get(), "[a b c]")

if __name__ == '__main__':
	ut.main()

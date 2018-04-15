import unittest


class ceshiStringMethods(unittest.TestCase):
	def ceshi_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def ceshi_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
	unittest.main()
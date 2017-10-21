import unittest
from sorted_set import SortedSet

class TestConstruction(unittest.TestCase):

	def test_empty(self):
		s = SortedSet([])

	def test_default_empty(self):
		s = SortedSet()

	def test_from_sequence(self):
		s = SortedSet([7, 8, 3, 2])

	def test_with_duplicates(self):
		s = SortedSet([8, 8, 8])
	
	def test_from_iterable(self):
		def generator_6842():
			yield 6
			yield 8
			yield 4
			yield 2
		generator = generator_6842()
		s = SortedSet(generator)


class TestContainedProtocol(unittest.TestCase):

	def setUp(self):
		self.sorted_class = SortedSet([6, 7, 8, 5, 3, 2])

	def test_positive_contained(self):
		self.assertTrue(6 in self.sorted_class)

	def test_negative_contained(self):
		self.assertFalse(15 in self.sorted_class)

	def test_positive_not_contained(self):
		self.assertTrue(4 not in self.sorted_class)

	def test_negative_not_contained(self):
		self.assertTrue(9 not in self.sorted_class)


class TestSizedProtocol(unittest.TestCase):

	def setUp(self):
		self.sorted_class = SortedSet()

	def test_empty(self):
		self.assertEqual(len(self.sorted_class), 0)

	def test_one(self):
		self.sorted_class._items = [45]
		self.assertEqual(len(self.sorted_class), 1)

	def test_ten(self):
		self.sorted_class._items = (range(10))
		self.assertEqual(len(self.sorted_class), 10)

	def test_with_duplicates(self):
		self.sorted_class = SortedSet([5, 5, 5])
		self.assertEqual(len(self.sorted_class._items), 1)


class TestIterableProtocol(unittest.TestCase):

	def setUp(self):
		self.sorted_class = SortedSet([2, 5, 3, 6])

	def test_iter(self):
		i = iter(self.sorted_class)
		self.assertEqual(next(i), 2)
		self.assertEqual(next(i), 3)
		self.assertEqual(next(i), 5)
		self.assertEqual(next(i), 6)
		self.assertRaises(StopIteration, lambda : next(i))

	def test_for_loops(self):
		index = 0
		expected = [2, 3, 5, 6]
		for item in self.sorted_class:
			self.assertEqual(item, expected[index])
			index += 1


if __name__ == '__main__':
	unittest.main()



class SortedSet:

	def __init__(self, items=None):
		self._items = sorted(set(items)) if items is not None else []

	def __contains__(self, args):
		return args in self._items

	def __len__(self):
		return len(self._items)

	def __iter__(self):
		return iter(self._items)
		
import unittest
from table_item import *

class TestTableItem(unittest.TestCase):
	def test_get_traffic(self):
		table_item = TableItem()
		self.assertEqual(table_item.get_traffic(), 0)

if __name__ == '__main__':
    unittest.main()
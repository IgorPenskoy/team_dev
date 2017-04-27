import unittest
from table_item import *

class TestTableItem(unittest.TestCase):
	def test_get_traffic_1(self):
		table_item = TableItem(None, None)
		self.assertEqual(table_item.get_traffic(), 0)

	def test_get_traffic_2(self):
		table_item = TableItem(10, None)
		self.assertEqual(table_item.get_traffic(), 0)

	def test_get_traffic_3(self):
		table_item = TableItem(None, 10)
		self.assertEqual(table_item.get_traffic(), 0)

	def test_get_traffic_4(self):
		table_item = TableItem(10, 3)
		self.assertEqual(table_item.get_traffic(), 30)

if __name__ == '__main__':
    unittest.main()
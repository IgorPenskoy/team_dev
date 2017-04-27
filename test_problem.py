import unittest
from problem import *

class TestProblem(unittest.TestCase):
	def test_solve(self):
		problem = Problem()
		self.assertEqual(problem.solve(), 0)

	def test_build_table_1(self):
		problem = Problem(None, None, None)
		self.assertEqual(problem.table, [])
		self.assertEqual(problem.width, 0);
		self.assertEqual(problem.height, 0);

	def test_build_table_2(self):
		problem = Problem(None, [30, 40, 20], None)
		self.assertEqual(problem.table, [[], [], []])
		self.assertEqual(problem.width, 0);
		self.assertEqual(problem.height, 3);

	def test_build_table_3(self):
		problem = Problem(None, None, [[2, 4, 1], [1, 3, 2], [5, 2, 4]])
		self.assertEqual(problem.table, [])
		self.assertEqual(problem.width, 0);
		self.assertEqual(problem.height, 0);

	def test_build_table_4(self):
		problem = Problem(None, [30, 40, 20], [[2, 4, 1], [1, 3, 2], [5, 2, 4]])
		self.assertEqual(problem.table, [[], [], []])
		self.assertEqual(problem.width, 0);
		self.assertEqual(problem.height, 3);
		
	def test_build_table_5(self):
		problem = Problem([25, 15, 50], None, None)
		self.assertEqual(problem.table, [])
		self.assertEqual(problem.width, 3);
		self.assertEqual(problem.height, 0);

	def test_build_table_6(self):
		problem = Problem([25, 15, 50], None, [[2, 4, 1], [1, 3, 2], [5, 2, 4]])
		self.assertEqual(problem.table, [])
		self.assertEqual(problem.width, 3);
		self.assertEqual(problem.height, 0);

	def test_build_table_7(self):
		with self.assertRaises(TypeError):
			problem = Problem([25, 15, 50], [30, 40, 20], None)

	def test_build_table_8(self):
		problem = Problem([25, 15, 50], [30, 40, 20], [[2, 4, 1], [1, 3, 2], [5, 2, 4]])
		for i in range(problem.width):
			for j in range(problem.height):
				self.assertEqual(problem.table[i][j].rate, problem.rates[i][j])
		self.assertEqual(problem.width, 3);
		self.assertEqual(problem.height, 3);

	def test_build_table_9(self):
		with self.assertRaises(IndexError):
			problem = Problem([25, 15, 50], [30, 40, 20], [[2, 4, 1], [1, 3, 2], [5, 2]])		

	def test_make_closeness(self):
		problem = Problem([10, 5, 3], [9, 3, 6], [[1,1,1],[1,1,1],[1,1,1]])
		problem.make_closeness()

	def test_check_closeness_1(self):
		problem = Problem([10, 5, 3], [9, 3, 6], [[1,1,1],[1,1,1],[1,1,1]])
		self.assertEqual(problem.check_closeness(), 0)

	def test_check_closeness_2(self):
		problem = Problem([10, 5, 3], [9, 3, 10], [[1,1,1],[1,1,1],[1,1,1]])
		self.assertEqual(problem.check_closeness(), 4)
		
	def test_make_basic_plan(self):
		problem = Problem([10, 5, 3], [9, 3, 6], [[1,1,1],[1,1,1],[1,1,1]])
		problem.make_basic_plan()

	def test_fix_degeneracy(self):
		problem = Problem()
		problem.fix_degeneracy()
		
	def test_check_degeneracy(self):
		problem = Problem()
		self.assertFalse(problem.check_degeneracy())

	def test_make_optimality(self):
		problem = Problem()
		problem.make_optimality()
	
	def test_check_optimality(self):
		problem = Problem()
		self.assertTrue(problem.check_optimality())
		
	def test_get_plan_potentials(self):
		problem = Problem()
		problem.get_plan_potentials()
		
	def test_get_expenses(self):
		problem = Problem()
		self.assertEqual(problem.get_expenses(), 0)

if __name__ == '__main__':
    unittest.main()
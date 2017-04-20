import unittest
from problem import *

class TestProblem(unittest.TestCase):
	def test_solve(self):
		problem = Problem()
		self.assertEqual(problem.solve(), 0)

	def test_build_table(self):
		problem = Problem()
		problem.build_table()
		self.assertEqual(problem.table, [])

	def test_make_closeness(self):
		problem = Problem()
		problem.make_closeness()

	def test_check_closeness(self):
		problem = Problem()
		self.assertTrue(problem.check_closeness())
		
	def test_make_basic_plan(self):
		problem = Problem()
		problem.make_basic_plan()
		self.assertEqual(problem.table, [])

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
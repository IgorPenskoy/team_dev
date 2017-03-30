from table_item import *

class Problem:
	def __init__(self, customers = None, providers = None, rates = None):
		self.customers = customers
		self.providers = providers
		self.rates = rates
		self.common_costs = None
		self.table = None
		self.build_table()

	def solve(self):
		return 0
		
	def build_table(self):
		pass
	
	def make_closeness(self):
		pass

	def check_closeness(self):
		return True
		
	def make_basic_plan(self):
		pass

	def fix_degeneracy(self):
		pass
		
	def check_degeneracy(self):
		return False

	def make_optimality(self):
		pass
	
	def check_optimality(self):
		return True
		
	def get_plan_potentials(self):
		pass
		
	def get_expenses(self):
		return 0
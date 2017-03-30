class Problem:
	def __init__(self, customers = None, providers = None, rates = None):
		self.customers = customers
		self.providers = providers
		self.rates = rates
		self.common_costs = None
		self.graph = None
		self.table = None
		self.create_table()

	def solve(self):
		return 0
		
	def create_table(self):
		pass
		
	def check_closeness(self):
		return True

	def correct_closeness(self):
		pass

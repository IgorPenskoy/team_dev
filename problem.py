from table_item import *
from math import inf

EPSILON = 0.01

class Problem:
	def __init__(self, customers = None, providers = None, rates = None):
		self.customers = customers
		self.providers = providers
		self.rates = rates
		self.common_costs = None
		self.table = None
		self.width = None
		self.height = None
		self.basis_item_count = 0
		self.build_table()

	def solve(self):
		return 0
		
	def build_table(self):
		if self.customers is None:
			self.width = 0
		else:
			self.width = len(self.customers)
		if self.providers is None:
			self.height = 0
		else:
			self.height = len(self.providers)
		self.table = [[TableItem() for x in range(self.width)] for y in range(self.height)]
		try:
			for i in range(self.height):
				for j in range(self.width):
					self.table[i][j].rate = self.rates[i][j]
		except IndexError:
			raise IndexError('Rates table is not in appropriate size')
		except TypeError:
			raise TypeError('Rates is None')

	def make_closeness(self):
		balance = self.check_closeness()
		if balance > 0:
			self.customers.append(balance)
			for i in range(len(self.rates)):
				self.rates[i].append(0)
		elif balance < 0:
			self.providers.append(-balance)
			self.rates.append([0 for x in range(len(self.customers))])

	def check_closeness(self):
		return sum(self.providers) - sum(self.customers)
		
	def make_basic_plan(self):
		p = list(self.providers)
		c = list(self.customers)
		for i in range(self.height):
			for j in range(self.width):
				if p[i] != 0 and c[j] != 0:
					supply = min(p[i], c[j])
					self.table[i][j].supply = supply
					p[i] -= supply
					c[j] -= supply

	def fix_degeneracy(self):
		for i in range(self.height):
			for j in range(self.width):
				if self.table[i][j].supply == 0:
					self.table[i][j].supply = None
		degeneracy = self.check_degeneracy()
		for i in range(self.height):
			for j in range(self.width):
				if self.table[i][j].supply is None and degeneracy > 0:
					self.table[i][j].supply = EPSILON
					self.providers[i] += EPSILON
					self.customers[j] += EPSILON
					degeneracy -= 1

	def check_degeneracy(self):
		self.basis_item_count = 0
		for i in range(self.height):
			for j in range(self.width):
				if self.table[i][j].supply is not None:
					self.basis_item_count += 1
		return self.width + self.height - self.basis_item_count - 1

	def make_optimality(self):
		pass
	
	def check_optimality(self):
		return True
		
	def get_plan_potentials(self):
		providers_potential = [None for x in range(self.height)]
		customers_potential = [None for x in range(self.width)]
		providers_potential[0] = 0
		flag = 1
		while flag:
			flag = 0
			for i in range(self.height):
				for j in range(self.width):
					if self.table[i][j].supply is not None:
						if providers_potential[i] is None and customers_potential[j] is None:
							flag = 1
						elif providers_potential[i] is not None and customers_potential[j] is None:
							customers_potential[j] = self.table[i][j].rate - providers_potential[i]
						elif providers_potential[i] is None and customers_potential[j] is not None:
							providers_potential[i] = self.table[i][j].rate - customers_potential[j]
		return providers_potential, customers_potential
		
	def get_expenses(self):
		return 0
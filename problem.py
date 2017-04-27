from table_item import *
from math import inf

EPSILON = 0.01
N = 100

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
		if self.providers is None or self.customers is None or self.rates is None:
			return 0
		self.make_closeness()
		self.make_basic_plan()
		self.fix_degeneracy()
		before_costs = self.get_expenses()
		n = 0
		while not self.check_optimality() and n < N:
			self.make_optimality()
			self.fix_degeneracy()
			n += 1
		self.common_costs = self.get_expenses()
		return before_costs - self.common_costs

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
			self.width += 1
			for i in range(self.height):
				self.table[i].append(TableItem(0))
		elif balance < 0:
			self.providers.append(-balance)
			self.height += 1
			self.table.append([TableItem(0) for x in range(self.width)])
			self.rates.append([0 for x in range(self.width)])

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
		delta_min = inf
		u = v = 0
		for i in range(self.height):
			for j in range(self.width):
				if self.table[i][j].delta < delta_min:
					delta_min = self.table[i][j].delta
					u = i
					v = j
		if delta_min < 0:
			self.table[u][v].supply = 0
			cycle = self.find_cycle(u, v)
			supply_min = inf
			for w in range(1, len(cycle), 2):
				tmp = self.table[cycle[w][0]][cycle[w][1]].supply
				if tmp < supply_min:
					supply_min = tmp
			for w in range(1, len(cycle), 2):
				self.table[cycle[w][0]][cycle[w][1]].supply -= supply_min
				self.table[cycle[w - 1][0]][cycle[w - 1][1]].supply += supply_min

	def find_cycle(self, i, j):
		cycle = [[i, j]]
		if self.look_horizontally(cycle, i, j, i, j):
			return cycle
		else:
			return []

	def look_horizontally(self, cycle, u, v, u1, v1):
		for i in range(0, self.width):
			if i != v and self.table[u][i].supply is not None:
				if i == v1:
					cycle.append([u, i])
					return True  # complete circuit
				if self.look_vertically(cycle, u, i, u1, v1):
					cycle.append([u, i])
					return True
		return False  # not found

	def look_vertically(self, cycle, u, v, u1, v1):
		for i in range(0, self.height):
			if i != u and self.table[i][v].supply is not None:
				if self.look_horizontally(cycle, i, v, u1, v1):
					cycle.append([i, v])
					return True
		return False  # not found

	def check_optimality(self):
		providers_potential, customers_potential = self.get_plan_potentials()
		flag = True
		for i in range(self.height):
			for j in range(self.width):
				self.table[i][j].delta = self.table[i][j].rate - (providers_potential[i] + customers_potential[j])
				if self.table[i][j].delta < 0:
					flag = False
		return flag

	def get_plan_potentials(self):
		providers_potential = [None for x in range(self.height)]
		customers_potential = [None for x in range(self.width)]
		providers_potential[0] = 0
		flag_1 = True
		flag_2 = True
		while flag_1 and flag_2:
			flag_1 = False
			flag_2 = False
			for i in range(self.height):
				for j in range(self.width):
					if self.table[i][j].supply is not None:
						if providers_potential[i] is None and customers_potential[j] is None:
							flag_1 = True
						elif providers_potential[i] is not None and customers_potential[j] is None:
							flag_2 = True
							customers_potential[j] = self.table[i][j].rate - providers_potential[i]
						elif providers_potential[i] is None and customers_potential[j] is not None:
							flag_2 = True
							providers_potential[i] = self.table[i][j].rate - customers_potential[j]
		print('potentials_gone')
		for i in range(self.height):
			if providers_potential[i] is None:
				providers_potential[i] = 0
		for i in range(self.width):
			if customers_potential[i] is None:
				customers_potential[i] = 0
		return providers_potential, customers_potential

	def get_expenses(self):
		result = 0
		for i in range(self.height):
			for j in range(self.width):
				result += self.table[i][j].get_traffic()
		return result
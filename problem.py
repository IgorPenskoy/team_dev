from table_item import *
from math import inf

## Accurancy of calculation
#
EPSILON = 0.001

## Number of optimization iterations
#
N = 100

##@brief A class for transportation problem
#
class Problem:
	## Constructor
	#
	#@param self class pointer
	#@param customers a list of customers demands
	#@param providers a list of providers opportunities
	#@param rates a matrix of rates for piece of transportation
	def __init__(self, customers = None, providers = None, rates = None):
		## @var customers
		# a list of customers demands
		self.customers = customers
		## @var  providers
		# a list of providers opportunities
		self.providers = providers
		## @var rates
		# a matrix of rates for piece of transportation
		self.rates = rates
		## @var common_costs
		# total cost of transportaions
		self.common_costs = None
		## @var table
		# table of transportations
		self.table = None
		## @var width
		# width of transportations table
		self.width = None
		## @var height
		# height of transportations table
		self.height = None
		## @var .basis_item_count
		# a count of basis elements in basic plan
		self.basis_item_count = 0
		self.build_table()
	
	## Calculate a table of transportations and total cost of transportations
	#
	#@param self class pointer
	#@return total costs of transportation
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
		self.result_rounding()
		return round(before_costs - self.common_costs, 2)

	## Init a table of transportation
	#
	#@param self class pointer
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

	## Make a transportation task closed
	#
	#@param self class pointer
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

	## Check a transportaion task for closenes
	#
	#@param self class pointer
	#@return balance of transportation
	def check_closeness(self):
		return sum(self.providers) - sum(self.customers)

	## Make a basic plan of transportation task
	#
	#@param self class pointer
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

	## Make plan non degenerative
	#
	#@param self class pointer
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

	## Check a basic plan for degeneracy
	#
	#@param self class pointer
	#@return count of needed basis elements
	def check_degeneracy(self):
		self.basis_item_count = 0
		for i in range(self.height):
			for j in range(self.width):
				if self.table[i][j].supply is not None:
					self.basis_item_count += 1
		return self.width + self.height - self.basis_item_count - 1

	## Optimize basic plan
	#
	#@param self class pointer
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

	## Find a cycle in basic plan
	#
	#@param self class pointer
	#@param i row in transportation table
	#@param j column in transportation table 
	#@return cycle or empty list
	def find_cycle(self, i, j):
		cycle = [[i, j]]
		try: 
			if self.look_horizontally(cycle, i, j, i, j):
				return cycle
			else:
				return []
		except RecursionError:
			return []

	## Find a horizontal path in transportation table for cycle
	#
	#@param self class pointer
	#@param u row in transportation table - begin of path
	#@param v column in transportation table - begin of path
	#@param u1 row in transportation table - end of path
	#@param v1 column in transportation table - end of path
	#@return True if cycle or False if not
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
		
	## Find a vertical path in transportation table for cycle
	#
	#@param self class pointer
	#@param u row in transportation table - begin of path
	#@param v column in transportation table - begin of path
	#@param u1 row in transportation table - end of path
	#@param v1 column in transportation table - end of path
	#@return True if cycle or False if not
	def look_vertically(self, cycle, u, v, u1, v1):
		for i in range(0, self.height):
			if i != u and self.table[i][v].supply is not None:
				if self.look_horizontally(cycle, i, v, u1, v1):
					cycle.append([i, v])
					return True
		return False  # not found

	## Check a basic plan for optimality
	#
	#@param self class pointer
	#@return True - if optimal, False - if not optimal
	def check_optimality(self):
		providers_potential, customers_potential = self.get_plan_potentials()
		flag = True
		for i in range(self.height):
			for j in range(self.width):
				self.table[i][j].delta = self.table[i][j].rate - (providers_potential[i] + customers_potential[j])
				if self.table[i][j].delta < 0:
					flag = False
		return flag
	## Get basic plan potentials
	#
	#@param self class pointer
	#@return two lists of plan potentials
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
		for i in range(self.height):
			if providers_potential[i] is None:
				providers_potential[i] = 0
		for i in range(self.width):
			if customers_potential[i] is None:
				customers_potential[i] = 0
		return providers_potential, customers_potential

	## Get expenses for trasportations
	#
	#@param self class pointer
	#@return cost of transportations
	def get_expenses(self):
		result = 0
		for i in range(self.height):
			for j in range(self.width):
				result += self.table[i][j].get_traffic()
		return result
		
	## Rounding of supplies
	#
	#@param self class pointer
	def result_rounding(self):
		for i in range(self.height):
			for j in range(self.width):
				if self.table[i][j].supply is not None:
					self.table[i][j].supply = round(self.table[i][j].supply, 2)

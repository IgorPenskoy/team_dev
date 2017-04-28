##@brief A class for item of transportation table
#
class TableItem:
	## Constructor
	#
	#@param self class pointer
	#@param rate a cost of transporting a piece of supply
	#@param supply quantity of supply
	#@param delta service variable
	def __init__(self, rate = None, supply = None, delta = None):
		## @var rate
		# a cost of transporting a piece of supply
		self.rate = rate
		## @var supply
		# quantity of supply
		self.supply = supply
		## @var delta
		# service variable
		self.delta = delta
	
	## Calculate cost of transportation
	#
	#@param self class pointer
	#@return cost of transportation
	def get_traffic(self):
		if self.rate is None or self.supply is None:
			return 0
		else:
			return self.rate * self.supply

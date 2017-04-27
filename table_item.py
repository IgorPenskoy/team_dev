class TableItem:
	def __init__(self, rate = None, supply = None, delta = None):
		self.rate = rate
		self.supply = supply
		self.delta = delta

	def get_traffic(self):
		if self.rate is None or self.supply is None:
			return 0
		else:
			return self.rate * self.supply

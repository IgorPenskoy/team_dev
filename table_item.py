class TableItem:
	def __init__(self, rate = None, supply = None, delta = None):
		self.rate = rate
		self.supply = supply
		self.delta = delta

	def get_traffic(self):
		return 0

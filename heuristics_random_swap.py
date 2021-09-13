import random

class Random_swap:
	def __init__ (self, row):

		self.k = len(row)
		self.pile1 = random.randint(0, self.k-1)
		self.pile2 = random.randint(0, self.k-1)
		while self.pile1 == self.pile2:
			self.pile2 = random.randint(0, self.k-1)
		self.row = row

	def randomagain(self):
			
		n = len(self.row[self.pile1])
		if n != 1:
			val1 = random.randint(0, n-1)
		else:
			val1 = 0

		n = len(self.row[self.pile2])
		if n != 1:
			val2 = random.randint(0, n-1)
		else:
			val2 = 0
		temp = self.row[self.pile1][val1]
		self.row[self.pile1][val1] = self.row[self.pile2][val2]
		self.row[self.pile2][val2] = temp 

		return self.row

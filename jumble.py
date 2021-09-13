#Jumble all the elemenets randomly 
import random

class Jumble_Swap:
	def __init__(self, k, x):
		self.order = []
		self.row = []

	def Process_jumble(self,k, x):

		while(len(self.order) != k):
			rand = random.randint(0, len(x)-1)
			if rand not in self.order:
				col = []
				col.append(x[rand])
				self.order.append(rand)
				self.row.append(col)

		i = 0
		rem = len(x) - len(self.order)

		#Randomly assign values into the row to later work on the heuristics  
		while(i < (rem)):
			rand = random.randint(0, len(x)-1)
			rand2 = random.randint(0, k-1)
			if rand not in self.order:
				self.row[rand2].append(x[rand])
				self.order.append(rand)
				i = i + 1

		return self.row

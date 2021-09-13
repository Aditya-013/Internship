import random

class Greedy_Swap:
	def __init__ (self, row):

		self.k = len(row)
		self.row = row

	def Max_Fitness_Calc(row, k):
		sum_arr = []
		for i in range(0, len(row)):
			temp = 0
			for j in range(0,len(row[i])):
				temp = temp + row[i][j]
			sum_arr.append(temp/k)

		max1 = max(sum_arr)
		min1 = min(sum_arr)
		return max1 - min1

	def greedy(self):
			
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

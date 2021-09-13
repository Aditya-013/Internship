## Sum of the Array
def sum(arr):
	sum_total = 0
	for i in range(0,len(arr)):
		sum_total = sum_total + arr[i]
	return sum_total

## Calculating the sum of each pile
def sum_calc(row):
	sum_arr = []
	for i in range(0, len(row)):
		temp = 0
		for j in range(0,len(row[i])):
			temp = temp + row[i][j]
		sum_arr.append(temp)

	return sum_arr

## Calculating the fitness Values of each pile
def fit_calc(sum_arr, k):
	fitness_val = []
	for i in range(0,len(sum_arr)):
		fitness_val.append(sum_arr[i]/k)
	return fitness_val

## Returns biggest Value
def big(sum_arr):
	big1 = 0
	for i in range(0, len(sum_arr)):
		if sum_arr[i] > sum_arr[big1]:
			big1 = i

	return big1

## Returns smallest value
def small(sum_arr):
	small1 = len(sum_arr) - 1
	for i in range(0, len(sum_arr)):
		if sum_arr[i] < sum_arr[small1]:
			small1 = i

	return small1


# def swap(val1, val2):

import random

## Values 

# n = 10
# k = 5
# arr = [99,92,95,90,96,98,93,92,95,99]

f = open("non_uni/non_uni/alm1_10_5_10", "r")
x=f.readlines()
n=x[0]
x= [int(i.strip("\n") ) for i in x[1:]]
n,k=list(map(int,input().split()))
x=[int(input()) for i in range(n)]
print(n,k,x)

# n = 10
# k = 5
# arr = [99,92,95,90,96,98,93,92,95,99]

sum_total = sum(arr)
iterations = 5
iterations_fall_back = 100
average = sum_total/k
average_in_pile = n/k

#36, 37, 38

# print("Average in Each pile :: ", average_in_pile)
# print("Average of sum/number  of piles:: ", average)
# print()

row = []
order = []
sum_of_arrays = []

## Assigning random values into the first layer of the pile 

##TODO :: ## assign k objects into each first 

while(len(order) != k):
	rand = random.randint(0, n-1)
	if rand not in order:
		col = []
		col.append(arr[rand])
		order.append(rand)
		row.append(col)

print("Initial Row after Random: ",row)
print()
smallest = [] # To hold the final pile values 
small_iteration = 100000 # To hold the fitness value of the final pile value
rand = random.randint(0, n-1)

## Assigning random values into the piles, but every pile gets the same number of values
## Except the final one which get the number of values of the remaining 
while len(order) < n:
	rand = random.randint(0, n-1)
	if rand not in order: 
		for i in range(0,len(row)):
			if len(row[i]) < average_in_pile:
				row[i].append(arr[rand])
				order.append(rand)
				break

# Initial set of piles
print("Initial Set of piles :: ", row)
# print(order)

sum_arr = sum_calc(row)
fitness_val = fit_calc(sum_arr, k) #Calculate fitness values

print("Initial sum of each piles:: ",sum_arr)
print("Initial Fitness Values :: ",fitness_val)
print()

'''
The while loop does the swapping method half the number of times 
And ramdonly switiches two values from piles half the number of times

It goes on till the fitness value (iterations) between the largest of it and smallest is less than 0.1
Or the loop has run 100 times 

The values with the least diff. b/w the fitness values is stored in smallest[]
Which is printed in the end of the loop
'''

while iterations > 0.1 and iterations_fall_back > 0:

	if int(iterations % 10 - iterations % 1) % 2 == 0:

		i = big(sum_arr)
		i0 = big(row[i])
		j = small(sum_arr)
		j0 = small(row[j])

	else:

		i = random.randint(0, len(row)-1)
		i0 = random.randint(0, len(row[i])-1)
		j = random.randint(0, len(row)-1)
		j0 = random.randint(0, len(row[j])-1)
    
	# print(i,j,i0,j0)

	# print("Biggest: ",sum_arr[i])
	# print("Smallest: ",sum_arr[j])

	# print("Biggest ka Biggest: ",row[i][i0])
	# print("Smallest ka smallest: ",row[j][j0])

	temp = row[i][i0]
	row[i][i0] = row[j][j0]
	row[j][j0] = temp 
	# print()

	sum_arr = sum_calc(row)
	fitness_val = fit_calc(sum_arr, k)

	# print(row)
	# print(sum_arr)
	# print(fitness_val)

	diff_val_big = big(fitness_val)
	diff_val_small = small(fitness_val)

	# print(fitness_val[diff_val_big] - fitness_val[diff_val_small])
	iterations = fitness_val[diff_val_big] - fitness_val[diff_val_small]

	if small_iteration > iterations:
		# print("Same lests:: ",small_iteration," ", iterations)
		# smallest = []
		small_iteration = iterations
		# smallest = row
		smallest = [i[:] for i in row]
		# print("____________InSIDE IF___________")
		# print(smallest)
		# print(row)
		# print("_______________________")
	

	# print("____________________________________________")
	# print(smallest)
	# print(row)
	# print("____________________________________________")
	# print()
	iterations_fall_back = iterations_fall_back - 1

print("___ Smallest amongst all the iterations ___")
print()
# print(small_iteration)
# print(smallest)
sum_arr = sum_calc(smallest)
fitness_val = fit_calc(sum_arr, k)
print("Smallest Set of Piles :: ",smallest)
print("Smallest Sum of the Set of Piles :: ",sum_arr)
print("Smallest Sum of the Fitness Values :: ",fitness_val)
diff_val_big = big(fitness_val)
diff_val_small = small(fitness_val)
print("Smallest difference b/w each :: ",fitness_val[diff_val_big] - fitness_val[diff_val_small])
print()

























import random
import numpy as np
import heuristics_random_swap as hrp
import jumble as jbl 
import Genetic01 as gen

## Calculating the sum of each pile
def Fitness_Calc(row, k):
	sum_arr = []
	for i in range(0, len(row)):
		temp = 0
		for j in range(0,len(row[i])):
			temp = temp + row[i][j]
		sum_arr.append(float(temp/k))

	max1 = float(max(sum_arr))
	min1 = float(min(sum_arr))
	return float(max1 - min1) 

# arr = [99, 3, 95, 90, 96, 98, 93, 92, 95]
f = open("non_uni/non_uni/alm1_10_5_12", "r")
x=f.readlines()
x=[i.strip("\n") for i in x]
x[1:]=[int(i) for i in x[1:]]
y=list(map(int,x[0].split()))
y.extend(x[1:])
k = y[1]
n = y[0]
arr = y[2:]
x = x[1:]
x = np.array(x)
x = x.astype(float)
row = []
order = []
sum_of_arrays = []

#k is the number of elemenets, x is []
obj1 = jbl.Jumble_Swap(k, x)			#jbl is an object in jumple.py
row = obj1.Process_jumble(k, x)
fitness_main = Fitness_Calc(row, k)

## Assigning random values into the first layer of the pile 
# while(len(order) != k):
# 	rand = random.randint(0, n-1)
# 	if rand not in order:
# 		col = []
# 		col.append(arr[rand])
# 		order.append(rand)
# 		row.append(col)

# print(row)
# i = 0
# rem = n - len(order)
# print(rem + len(order))

# #Randomly assign values into the row to later work on the heuristics  
# while(i < (rem)):
# 	rand = random.randint(0, n-1)
# 	rand2 = random.randint(0, k-1)
# 	if rand not in order:
# 		row[rand2].append(arr[rand])
# 		order.append(rand)
# 		i = i + 1

print("")
print('                         ----Initial Solution ----')
print('The inital order of the piles: {}'.format(row))	#Randomly generated set of piles 
print('Fitness of the piles {}'.format(fitness_main))
print("")


# Four Heuristics to be assigned after this with the help of RL 
# 1) Random Swap	2) Pertubation Search	3) Genetic Algorithm 

# RL has a 0.75 learning rate and based on the reward and regret of each of the individual outputs, the algorithm moves forward 
# Example: row1 = output from Random swap, if the value is closer to the required output
# row = row1; -> reward is updated for random swap and RL moves forward. 
# The next algorithm's soluion compares with the new [row]
# Finally based on the best solution, the RL algorithm keeps choosing that to get to the best possible outcome. 
# After a set number of iterations, or after the the solution gets to a particular point, the algorithm stops. 

# The agent's class includes only two methods: the constructor and the method that performs the step in the environment. 

# Initially the total reward is 0.
# The step functions accepts environment instances as an argument and allowes agent to perform the following actions

# Observe the environment
# Make a decision about the action to take, based on the observation
# Submit the action to the environment
# Get the reward for the current step  


# New Data :: September 13, 2021, Monday 
# --------- REGARDING REINFORCEMENT LEARNING ----------------

# def one_step_lookahead(): Calculate and return the values of the expected values of each action
# Bellman's equation -> The expected value of your action if the sum of your immediate reward and the value of the next state.
# Calculate the delta of all the states so far (ignore the previous ones, they don't matter)
# Update the value function, check if you can stop or not. 

# Basically -> calculate the score of each of the heuristics assigned, find which values has the best (lowest minimum averages difference b/w piles)
# Update the current pile with the pile which has the best outcome. (Greedy)
# Run again until the limit condition. 

# To-Do
# Write the code for Pertubation Search
# Write the code for Genetic algorithm
# Write the code for RL 

steps = 20000
jumble = 0
swaps = 0

number_of_population = 10
i = 10
population = []
population_fitness = []

while i > 0:
	obj1 = jbl.Jumble_Swap(k, x)			#jbl is an object in jumple.py
	row = obj1.Process_jumble(k, x)

	population.append(row)
	population_fitness.append(Fitness_Calc(row, k))
	i = i-1

temp1 = []
temp2 = []

# Selection of the 2 best parents with the best fitness values (for now)
for i in range(10):
	for j in range(i+1, 10):
		if population_fitness[j] < population_fitness[i]:
			temp1 = population_fitness[j]
			population_fitness[j] = population_fitness[i]
			population_fitness[i] = temp1

			temp2 = population[j]
			population[j] = population[i]
			population[i] = temp2

print("")
print("          ------Population pool------")
i = 0
while i < 10:
	print(population[i], "  Fitness Value :: {:.2f}" .format(population_fitness[i]))
	i = i + 1

obj2 = gen.Genetic_Algo(population[0], population[1], k, x)
child = obj2.CrossOver(population[0], population[1], k, x)
# print(child)

"""

while steps > 0:

	random_value = random.randint(0,1)

	if random_value % 2 == 0:
		obj = hrp.Random_swap(row)
		row1 = obj.randomagain()
	else:
		obj1 = jbl.Jumble_Swap(k, x)
		row1 = obj1.Process_jumble(k, x)

	fitness = Fitness_Calc(row1, k)
	if fitness < fitness_main:
		if random_value % 2 == 0:
			jumble = jumble + 1
		else:
			swaps = swaps + 1
		print()
		print('Step number {}'.format(20001 - steps))
		print('New Pile {} Fitness {}'.format(row1, fitness))
		print('Old Pile {} Fitness : {}'.format(row, fitness_main))
		fitness_main = fitness
		row = row1
	steps = steps - 1

	# Output of this while loop is sent back to the RL algorithm to decide 
	# wether or not to reward the method used. 
	# For now a random value is used to choose which algorithm to use. 
	# Later the choice of algorithm will be provided by the RL function.








print()
print()
print()
print()
print('                         ----Final Solution ----')
print('The order  of the piles: {}'.format(row))	#Randomly generated set of piles 
print('Fitness of the finalpile {}'.format(fitness_main))
print('                         ---')
print('Number of better jumble swaps {}'.format(jumble))
print('Number of better normal swaps {}'.format(swaps))
print()






"""


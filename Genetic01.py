import random

class Genetic_Algo:
    def __init__(self, parent1, parent2, k, x):
        self.child = []
    def CrossOver(self, parent1, parent2, k, x):
        print('Enteed')
        x = x.tolist()
        sum1avg = []
        sum2avg = []
        sum = 0
        count = 0
        for i in range(k):
            sum = 0
            count = 0
            for j in range(len(parent1[i])):
                sum = sum + parent1[i][j]
                count = count + 1
            sum1avg.append(sum/count)
            sum = 0
            count = 0
            for j in range(len(parent2[i])):
                sum = sum + parent2[i][j]
                count = count + 1
            sum2avg.append(sum/count)

        for i in range(k):
            parent2[i].sort()
            parent1[i].sort()
        temp = 0
        temp1 = []
        for i in range(k):
            for j in range(i+1, k):
                if(sum1avg[i] > sum1avg[j]):
                    temp = sum1avg[i]
                    sum1avg[i] = sum1avg[j]
                    sum1avg[j] = temp
                    temp1 = parent1[i]
                    parent1[i] = parent1[j]
                    parent1[j] = temp1

        for i in range(k):
            for j in range(i+1, k):
                if(sum2avg[i] < sum2avg[j]):
                    temp = sum2avg[i]
                    sum2avg[i] = sum2avg[j]
                    sum2avg[j] = temp

                    temp1 = parent2[i]
                    parent2[i] = parent2[j]
                    parent2[j] = temp1

        print('Parent 1:')
        print(parent1)
        print('Sum Avg:')
        print(sum1avg)
        print('Parent 2:')
        print(parent2)
        print('Sum Avg:')
        print(sum2avg)

        child_temp = []
        temp2 = []
        for i in range(k):
            temp2 = []
            temp2.append(parent2[i][0])
            temp2.append(parent1[i][len(parent1[i])-1])
            child_temp.append(temp2)
        k = 0
        flag = 0
        print('Ignore everything on top')
        # arr = [[10, 14, 10, 10], [19, 32], [67, 9]]
        # x = [92, 91, 94, 95, 92, 94, 100, 93, 90, 3]
        # for i in range(len(arr)):
	    #     for j in range(len(arr[i])):
		#         flag = 0
		#         for k in range(len(x)):
		# 	        if x[k] == arr[i][j]:
		# 		        x[k] = -1
		# 		        flag = 1
		# 		        break
		#         if flag == 0:
		# 	        arr[i][j] = -1

        temp_x = x.copy()
        for i in range(len(child_temp)):
            for j in range(len(child_temp[i])):
                flag = 0
                for k in range(len(x)):
                    if child_temp[i][j] == x[k]:
                        x[k] = -1
                        flag = 1
                        break
                if flag == 0:
                    child_temp[i][j] = -1


        print(child_temp)
        print(x)
        print(temp_x)
        print('Ignore everything below')


            # print('^^^^^^^^^^^^^^^^^^^^^')
            # print(parent1)
            # print(sum1avg)
            # print('---------')
            # print(parent2)
            # print(sum2avg)
            # print('---------')
        return self.child
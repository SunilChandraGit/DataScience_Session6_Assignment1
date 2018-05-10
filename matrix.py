import numpy as np

#Input vector
arr = [1, 2, 5, 8, 4, 6]

#intialize increasing variable
increasing = [False, True, True, True, False, True, False]

#create list
my_list = []

#calculate value of each element in matrix and append it to my_list
for i in arr:
    for x in range(6):
        if(increasing[x]):
            my_list.append(i**(x+1))
        else:
            my_list.append(i)

#create numpy array from list
arrt = np.array(my_list)

#change shape for matrix
arrt.shape=(6, 6)

#create matrix from 2d array
mat = np.matrix(arrt)

#print resultant matrix
print(mat)
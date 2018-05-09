import numpy as np

#Input vector
arr = [1, 2, 5]

#Initial Matrix
mat = np.matrix([[1, 3, 4],[1, 7, 4],[1, 5, 8]])

#modify each element in matrix 
for x in range(3):
    for y in range(3):
        mat[y, x]=mat[y, x]**arr[x]

#print the resultant matrix
print(mat)
        
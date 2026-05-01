import numpy as np

# linalg.det computes the determinant of an array
# print(np.linalg.det([[1,2], [2,1]])) -> -3.0
#
# linalg.eig computes the eigenvalues and right eigenvectors of a square array
# 
# vals, vecs = np.linalg.eig([[1,2], [2,1]])
# print vals        output: [3. -1.]
# print vecs        output: [[ 0.70710678 -0.70710678][ 0.70710678  0.70710678]]
#
# linalg.inv computes the (multiplicative) inverse of a matrix
#
# print(np.linalg.inv([[1 , 2], [2, 1]])    output: [[-0.33333333  0.66666667][ 0.66666667 -0.33333333]]
#
# find the determinant

N = int(input())

temp = []

for i in range(N):
    
    temp.append(list(map(float, input().split())))
    
final = np.array(temp)

det = np.linalg.det(final)

print(round(det, 2))
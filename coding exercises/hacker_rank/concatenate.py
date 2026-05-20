# Two or more arrays can be concatenated together using the concatenate function with a tuple with a tuple of the arrays to be joined:
# 
# array_1 = numpy.array([1,2,3])
# array_2 = numpy.array([4,5,6])
# array_3 = numpy.array([7,8,9])

# print numpy.concatenate((array_1, array_2, array_3))    

# #Output
# [1 2 3 4 5 6 7 8 9]
#
# If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated
#
# array_1 = numpy.array([[1,2,3],[0,0,0]])
# array_2 = numpy.array([[0,0,0],[7,8,9]])

# print numpy.concatenate((array_1, array_2), axis = 1)   

# #Output
# [[1 2 3 0 0 0]
#  [0 0 0 7 8 9]]   
import numpy

NMP = list(map(int, input().split()))

# print(NMP)

M = []
N = []


for i in range(0, NMP[0]):
    M.append(list(map(int, input().split())))
    
for i in range(0, NMP[1]):
    N.append(list(map(int, input().split())))

# print(M)
# print(N)

print(numpy.concatenate((numpy.array(M), numpy.array(N)), axis = 0)) 
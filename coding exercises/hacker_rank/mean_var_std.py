# The mean tool computes the arithmetric mean along a specific axis
# my_array = numpy.array([1,2],[3,4])
#
# ***By default the axis is None, so the mean of a flattened array is computed
# 
# print(numpy.mean(my_array, axis = 0))   # output: [2. 3.]
# print(numpy.mean(my_array, axis = 1))   # output: [1.5 3.5]
# print(numpy.mean(my_array, axis = None))   # output: 2.5
# print(numpy.mean(my_array))   # output: 2.5

# The var tool computes the arithmetic variance along the specified axis
# print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
# print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
# print numpy.var(my_array, axis = None)      #Output : 1.25
# print numpy.var(my_array)                   #Output : 1.25

# The std tool computes the arithmetic standard deviation along the specified axis
# print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
# print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
# print numpy.std(my_array, axis = None)      #Output : 1.11803398875
# print numpy.std(my_array)                   #Output : 1.11803398875
import numpy

n, m = input().split()

N = int(n)
M = int(m)

the_array = []

for i in range(0,N):
    the_array.append(list(map(float, input().split())))
    
# print(the_array)

print(numpy.mean(the_array, axis = 1))
print(numpy.var(the_array, axis = 0))
print(round(numpy.std(the_array, axis = None), 11))
#The default axis value is none
# The tool min returns the minimum value along a given axis
# my_array = numpy.array([[2, 5], 
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])

# print numpy.min(my_array, axis = 0)         #Output : [1 0]
# print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
# print numpy.min(my_array, axis = None)      #Output : 0
# print numpy.min(my_array)                   #Output : 0
#
# The tool max returns the maximum value along a given axis
# my_array = numpy.array([[2, 5], 
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])

# print numpy.min(my_array, axis = 0)         #Output : [4 7]
# print numpy.min(my_array, axis = 1)         #Output : [5 7 3 4]
# print numpy.min(my_array, axis = None)      #Output : 7
# print numpy.min(my_array)                   #Output : 7

import numpy

n, m = input().split()

N = int(n)
M = int(m)

data = []

for i in range(0, N):
    data.append(list(map(int, input().split())))
    
# print(data)

min_1 = numpy.min(data, axis = 1)
print(numpy.max(min_1))
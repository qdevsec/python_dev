# Transpose - we can generate the transposition of an array using the tool numpy.transpose
# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print numpy.transpose(my_array)

# #Output
# [[1 4]
#  [2 5]
#  [3 6]]
#
# Flatten - this tool creates a copy of the input array flattened to one dimension numpy.flatten
# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print my_array.flatten()

# #Output
# [1 2 3 4 5 6]
import numpy

NM = list(map(int, input().split()))

arr = []

for i in range(NM[0]):
    arr.append(list(map(int, input().split())))
    
# print(arr)

print(numpy.transpose(numpy.array(arr)))
print(numpy.array(arr).flatten())
# The zeros tool returns a new array with a given shape and type filled with 0's
# print numpy.zeros((1,2))                    #Default type is float
# #Output : [[ 0.  0.]] 

# print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
# #Output : [[0 0]]
#
# The ones tool returns a new array with a given shape and type filled with 1's
# print numpy.ones((1,2))                    #Default type is float
# #Output : [[ 1.  1.]] 

# print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
# #Output : [[1 1]]   
import numpy

arr = list(map(int, input().split()))

tup_list = (*arr,)

# print(tup_list)

print(numpy.zeros(tup_list,dtype=int))
print(numpy.ones(tup_list,dtype=int))
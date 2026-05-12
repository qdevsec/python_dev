# Default axis value is None
# The sum tool returns the sum of array elements over a given axis
# my_array = numpy.array([ [1, 2], [3, 4] ])

# print numpy.sum(my_array, axis = 0)         #Output : [4 6]
# print numpy.sum(my_array, axis = 1)         #Output : [3 7]
# print numpy.sum(my_array, axis = None)      #Output : 10
# print numpy.sum(my_array)                   #Output : 10
#
# The prod tool returns the product of array elements over a given axis
# my_array = numpy.array([ [1, 2], [3, 4] ])

# print numpy.prod(my_array, axis = 0)            #Output : [3 8]
# print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
# print numpy.prod(my_array, axis = None)         #Output : 24
# print numpy.prod(my_array)                      #Output : 24
import numpy

the_list = []

n, m = input().split()

N  = int(n)
M  = int(m)

for i in range(0,N):
    the_list.append(list(map(int, input().split())))
    
# print(the_list)

sum_0 = numpy.sum(the_list, axis = 0)
print(numpy.prod(sum_0))
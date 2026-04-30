import numpy

# A NumPy array is a grid ov values, similar to lists except every element of an array must be the same type
#
# a = numpy.array([1,2,3,4,5])
# print(a[1]) == 2
#
# a = numpy.array([1,2,3,4,5], float)
# print(b[1]) == 2.0

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr,float)
    
    # reverses the order of elements
    b = numpy.flip(arr)
    
    # casts the elements in the array to a specific type
    c = b.astype('float64')
    # print(c)
    
    return c

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
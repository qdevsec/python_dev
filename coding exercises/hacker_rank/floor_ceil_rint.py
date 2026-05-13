# The tool floor returns the floor of the input element-wise
# The floor of x is the largest integer i where i <= x
#
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
#
# The tool ceil returns the ceiling of the input element-wise
# The ceiling of x is the smallest integer i where i >= x
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
#
# The rint tool rounds to the nearest integer of input element-wise
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
import numpy
numpy.set_printoptions(legacy='1.13')

A = list(map(float, input().split()))

# print(A)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
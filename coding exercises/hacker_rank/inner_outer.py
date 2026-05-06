# The inner tool returns the inner product of 2 arrays
# A = numpy.array([0,1])
# B = numpy.array([3,4])
# print(numpy.inner(A,B)) # output : 4
#
# The outer tool returns the outer product of two arrays
# A = numpy.array([0,1])
# B = numpy.array([3,4])
# print(numpy.inner(A,B)) # output : [[0 0][3 4]]
import numpy

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(numpy.inner(A, B))
print(numpy.outer(A, B))

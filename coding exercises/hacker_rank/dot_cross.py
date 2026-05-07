# The dot tool returns the dot product of two arrays
# A = numpy.array([1,2])
# B = numpy.array([3,4])
# print(numpy.dot(A, B))   # output: 11
#
# The cross tool returns the cross product of two arrays
# A = numpy.array([1,2])
# B = numpy.array([3,4])
# print(numpy.cross(A, B))   # output: -2
import numpy

N = int(input())

A = []

B = []

for i in range(0, N):
    A.append(list(map(int, input().split())))
    
# print(A)

for i in range(0, N):
    B.append(list(map(int, input().split())))
    
# print(B)

print(numpy.dot(A, B))

# the identity tool returns an identity array.
# an identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0, default type is float
# print numpy.identity(3) #3 is for  dimension 3 X 3

# #Output
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
#
# The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere.
# The diagonal can be main, upper or lower depending on the optional parameter k
# A positive k is for the upper diagonal, a negative k is for the lower, and a 0 k (default) is for the main diagonal
#
# print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

# #Output
# [[ 0.  1.  0.  0.  0.  0.  0.]
#  [ 0.  0.  1.  0.  0.  0.  0.]
#  [ 0.  0.  0.  1.  0.  0.  0.]
#  [ 0.  0.  0.  0.  1.  0.  0.]
#  [ 0.  0.  0.  0.  0.  1.  0.]
#  [ 0.  0.  0.  0.  0.  0.  1.]
#  [ 0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.]]

# print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
import numpy
numpy.set_printoptions(legacy='1.13')

NM = list(map(int, input().split()))

print(numpy.eye(NM[0], NM[1], k=0))
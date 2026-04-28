#####
# itertools.combinations(iterable, r)
# returns th r length subsequences of elements from the input iterable
# Combinations are emitted in a lexicographic sorted order. If the input iterable is sorted, the combination tuples will be produced in sorted order
#
# usage
# print(list(combinations('12345',2)))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
#
# A = [1,1,3,3,3]
# print(list(combinations(A,4)))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

from itertools import combinations

ans = input().split()

iterable = "".join(sorted(ans[0]))
r = int(ans[1])

a = 1

for i in range(1,r+1):
    
    
        
    it = list(combinations(iterable,a))
    
    for i in it:
        
        print(*i, sep="")

    a = a + 1
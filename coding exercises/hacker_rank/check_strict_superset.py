# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the n sets.
# 
# Print True, if a is a strict superset of each of the n sets. Otherwise, print False.
# 
# A strict superset has at least one element that does not exist in its subset. 

# A = set(input().split())
A = set(map(int, input().split()))

# print(A)
n = int(input())

answer = True



for i in range(n):
    
    subsection = set(map(int, input().split()))
    
    # if I combine everything from subsection and A together, does the result look like A
    answer = answer & ((subsection | A) == A)
    
    # print(subsection)
    # print(subsection | A)
    # print(A) 
    
print(answer)
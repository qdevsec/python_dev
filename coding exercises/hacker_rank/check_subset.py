# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

T = int(input())

for i in range(T):
    A_num = int(input())
    
    A = set(map(int, input().split()))
    
    B_num = int(input())
    
    B = set(map(int, input().split()))
    
    if A.issubset(B) == True:
        print("True")
    else:
        print("False")
    
    # print(A_num, A, B_num, B)
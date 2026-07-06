# any()

# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False. 

# all()

# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True. 

# Task

# You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
# https://en.wikipedia.org/wiki/Palindromic_number

# Input Format

# The first line contains an integer N. N is the total number of integers in the list.
# The second line contains the space separated list of N integers.

# Challenge to solve in 3 lines

N = int(input())

# l = input().split()

# check = "False"
l = list(map(int, input().split()))

print(all(i > 0 for i in l) and any( i == i[::-1] for i in map(str, l)))

# for i in l:
#     if i < 0:
#         continue
#     else:
#         num_s = str(i)
        
#         if num_s == num_s[::-1]:
#             check = "True"
        
# print(check)
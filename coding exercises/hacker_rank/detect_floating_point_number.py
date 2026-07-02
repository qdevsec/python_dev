# You are given a string N.
# Your task is to verify that N is a floating point number. 
# In this task, a valid float number must satisfy all of the following requirements: 
# https://www.hackerrank.com/challenges/introduction-to-regex/tutorial
# In this task a valid float number must satisfy all of the following requirements

# > Number can start + , - or . symbol
# For example:
# ✔+4.50
# ✔-1.0
# ✔.5
# ✔-.7
# ✔+.4
# ✖ -+4.5

# > Number must contain at least 1 decimal value
# For example:
# ✖ 12.
# ✔12.0  

# > Number must have exactly one . symbol.
# > Number must not give any exceptions when converted using float(N).
import re

N = int(input())

begin = ('-', '+', '.')

# print(N)

for _ in range(N):
    print(bool(re.search(r"^[+-.]?\d*[.]+\d+$",input())))

# for i in range(N):
    # 
    # s = input()
    # print(s)
    # 
    # if s.strip().startswith(begin):
    #     if re.match(r'^[-+]?\d+\.\d+$', input()):
    #         print("True")
    #     else:
    #         print("False")
    # else:
    #     print("False")

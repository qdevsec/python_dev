# https://docs.python.org/2/library/re.html#re.MatchObject.start

# Code
# >>> import re
# >>> m = re.search(r'\d+','1234')
# >>> m.end()
# 4
# >>> m.start()
# 0

# Task
# You are given a string S.
# Your task is to find the indices of the start and end of string k in S.

# Input Format

# The first line contains the string S.
# The second line contains the string k.

# Output Format

# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).
import re

S = input()
k = input()


pattern = re.compile(k)
match = pattern.search(S)

if match == None:
    print((-1, -1))
else:
    while match:
        print((match.start(), match.end() - 1))
        match = pattern.search(S, match.start()+1)
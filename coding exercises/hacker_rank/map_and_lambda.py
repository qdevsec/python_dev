# The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: 
# first, the function that is to be applied and secondly, the iterables.
# Let's say you are given a list of names, and you have to print a list that contains the length of each name. 

# >> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
# [4, 3, 3]  

# Lambda is a single expression anonymous function often used as an inline function. 
# In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

# >> sum = lambda a, b, c: a + b + c
# >> sum(1, 2, 3)
# 6

# Input: 5
# Output: [0, 1, 1, 8, 27]
# Explanation: The first 5 fibonacci numbers are [0, 1, 1, 2, 3], and their cubes are [0, 1, 1, 8, 27].

from itertools import accumulate, repeat

cube = lambda x: x ** int(3) 

# complete the lambda function 

def fibonacci(n):
    if n <= 0: return []
    # return a list of fibonacci numbers
    # accumulate(iterable, function, initial)
    # state - result of the previous iteration or initial
    # _ - the current item coming out of your iterable, the _ is used since the focus is the loop happening not the actual value
    gen = accumulate(repeat(0, n-1), lambda state, _: (state[1], state[0] + state[1]), initial=(0, 1))
    
    # the actual Fibonacci sequence is the first number in each pair in gen
    # pair[0] - from (0, 1) get pair[0] so 0
    # pair[1] - from (1, 1) get pair[0] so 1 
    return [pair[0] for pair in gen]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
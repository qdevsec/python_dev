from itertools import permutations

#### usage
# print(list(['1', '2', '3'])) <-- creates all possible combinations of 3
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
#
# print(list(permutations(['1', '2', '3'], 2))) <-- creates all possible combination in set of 2
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# 
# print(list(permutations('abc', 3))) <-- splits string into chars, and creates all possible combinations of 3
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

# sample input
# HACK 2

a, b = input().split()

# convert permutations size
k = int(b)

# sort the letters so that permutations will be ordered lexicographically
# the sorted function creates a list of chars, join will recreate string
sorted_word = "".join(sorted(a))

# debug
# print(sorted_word)

# create list of permutations
list_perms = list(permutations(sorted_word, k))

#debug
# print(list_perms)

for i in list_perms:
    # unpack values in tuple with *
    # print() optional arg sep="", removes space the function adds by default
    # can also specify sep="/" or sep="-" <-- can use to create date
    print(*i, sep="")



len_a = int(input())
# print(len_a)

# maps integer to the outcome of splitting of input
a = set(map(int, input().split())) 
# print(a)

# remaining inputs will be an operation a set
n = int(input())

for _ in range(n):
    operation = input().split()[0]
    other_set = set(map(int, input().split()))

    if operation == "update":
        a.update(other_set)
    elif operation == "intersection_update":
        a.intersection_update(other_set)
    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        a.difference_update(other_set)

print(sum(a))

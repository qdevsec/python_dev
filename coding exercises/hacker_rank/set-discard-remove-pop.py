n = int(input())

# print(f"num of elements in the set {n}")

s = set(map(int, input().split()))

num_commands = int(input())

for i in range(num_commands):
    pair = input().split()
    # print(pair)
    
    if len(pair) > 1:
        # print(pair[1])
        int_i = int(pair[1])
        # print(type(int_i))
               
        # decision
        if int_i in s:
            # print("print is in set...")
            if pair[0] == 'remove':
                s.remove(int_i)
            if pair[0] == 'discard':
                s.discard(int_i)

    else:
        if pair[0] == 'pop':
            s.pop()

    # print(s)

# print(s)
print(sum(s))

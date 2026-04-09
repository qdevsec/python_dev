# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_shoes = int(input())
# print(f"# of shoes: {num_shoes}")

shoe_sizes = input().split()
# print(f" shoe sizes: {shoe_sizes}")

dict_shoes = dict(Counter(shoe_sizes))

# print(f"type: {type(dict_shoes)} starting dict: {dict_shoes}")

num_customers = int(input())
# print(f"# of customers: {num_customers}")

sum = 0

for i in range(num_customers):
    # print("item")
    customer = input().split()
    if customer[0] in dict_shoes.keys():
        # print(f"{customer[0]} is a key in dict")
        
        if dict_shoes[customer[0]] == 0:
            # print("no more shoes")
            pass
        else:
            dict_shoes[customer[0]] -= 1
            sum = int(sum) + int(customer[1])
        
        # print(f"updated dictionary {dict_shoes}")
        

print(sum) 

# return sum


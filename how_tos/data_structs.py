# Lists - ordered, duplicates allowed can locate by index
# Sets - unique values, cant use indexing to locate
# Dicts - key pair value, can locate by key

# lists & set functions
len()  # number of elements
max()  # largest value
min()  # smallest values
sum()  # sum (for numbers only)

# list - ordered, mutable, allows duplicates
users = ["alice", "bob"]
users.append("charlie") # add item to end
users.sort()            # sort in place
users.remove("bob")     # removes 1st occurrence of value
users.reverse()         # reverses the list
users.clear()           # remove all items
users.pop([i])          # removes & returns item at specified index

# set - unordered, no duplicates
active = {"alice", "bob"}
active.add("charlie") # add element
active.discard("bob") # no error if you found
active.remove(x)      # error if not found
active.pop()          # remove random element
active.clear()        # empty set

# set operations
# union() or |  <-- combine
# a = {1, 2, 3}  b = {3, 4}
# print (a | b) 
# intersection() or &  <-- common elements
# difference() or -   <-- subtract

# dict - key-value pairs
scores = {"alice": 10}   # add key, value pair
scores["bob"] = 20       # access value with a key
# if key exists, returns value, if it doesnt returns default (None)
scores.items()          # key-value pairs
scores.keys()           # all keys
scores.pop("bob", None) # remove key
scores.update(dict2)    # merge dictionaries
scores.popitem()        # remove last item


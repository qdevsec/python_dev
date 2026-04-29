### Collections deque()
# deque is a double-ended queue, it can be used to add or remove elements from both ends
# deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same
# O(1) performance in either direction
# https://docs.python.org/2/library/collections.html#collections.deque
# deque() methods
# Deque Recipes
#
# d = deque()
# d.append(1)
# d.appendleft(2) -> [2,1]
# d.clear()
# d.extend('1')
# d.extendleft('234')
# d.count('1')
# d.pop() -> pops the last item
# d.popleft() -> pops the first item
# d.extend('7896')
# d.remove('2') -> remove value that matches
# d.reverse() -> reverses the list/array
# d.rotate(3) rotates list or array by a certain number
# ['6', '9', '8', '7', '3'] --> ['8', '7', '3', '6', '9']

from collections import deque

num_operations = int(input())

d = deque()

for i in range(0,num_operations):
    
    ans = input().split()
    
    if ans[0] == 'append':
        d.append(int(ans[1]))
    elif ans[0] == 'popleft':
        d.popleft()
    elif ans[0] == 'appendleft':
        d.appendleft(int(ans[1]))
    if ans[0] == 'pop':
        d.pop()
        
print(*d)

# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1.

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. 
# The room numbers will appear K times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of K and the room number list.

K = int(input())

# turn each element to int
S = list(map(int, input().split()))

the_set = set(S)


# it is missing exactly K - 1
# ideal : perfect sum = sum(the_set) x K
# real : captain appears only 1 time 
# deficit : subtract real from ideal to get value for captain
#    ideal sum - real sum = (sum(the_set) * K) - sum(S)
#    since captain appears once, it is missing exactly K - 1
#    dividing the deficit by K - 1 isolates the exact value of the captain
captain = ((sum(the_set) * K) - sum(S)) // (K - 1)
print(captain)

# Original List - S
# Unique Set - the_set
# Calculate - sum(the_set) * K
# Calculate - sum(S)
# Subtract sums - (sum(the_set) * K) - (sum(S))
# Divide K - 1 - (sum(the_set) * K) - (sum(S)) // (K - 1)
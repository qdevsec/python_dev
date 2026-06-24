# group()
# https://docs.python.org/2/library/re.html#re.MatchObject.group
# A group() expression returns one or more subgroups of the match. 

# groups()
# https://docs.python.org/2/library/re.html#re.MatchObject.groups
# A groups() expression returns a tuple containing all the subgroups of the match. 

# groupdict()
# https://docs.python.org/2/library/re.html#re.MatchObject.groupdict
# A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name. 
import re

S = input()

match = re.search(r'([a-zA-Z0-9])\1',S)

if match:
    print(match.group(1))
else:
    print(-1)
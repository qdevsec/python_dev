# https://docs.python.org/2/library/re.html#re.findall
#
# The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings. 
# >>> import re
# >>> re.findall(r'\w','http://www.hackerrank.com/')
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

# https://docs.python.org/2/library/re.html#re.finditer
#
# The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 
# >>> import re
# >>> re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
# >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

# Task
# You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of that contains or more vowels.
# Also, these substrings must lie in between consonants and should contain vowels only.
# 
# Note :
# Vowels are defined as: AEIOU and aeiou.
# Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.
import re 

# Patterns
# [^aeiouAEIOU\d\W_] - Consonant (Any letter that is not a vowel, digit, underscore, or whitespace).
# [aeiouAEIOU] - Vowel (Any upper or lowercase vowel).
# [aeiouAEIOU]{2,} - 2+ vowels (Matches two or more consecutive vowels).

# Lookarounds - used to lookahead and lookbehind assertions
# Positive Lookbehind for consonant: (?<=[^aeiouAEIOU\d\W_])
# Positive Lookahead for consonant: (?=[^aeiouAEIOU\d\W_])

pattern = r'(?<=[^aeiouAEIOU\d\W_])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU\d\W_])'

matches = re.findall(pattern, input())

if matches:
    for m in matches:
        print(m)
else:
    print('-1')
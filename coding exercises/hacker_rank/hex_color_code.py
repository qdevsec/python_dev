# CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

# Specifications of HEX Color Code

# ■ It must start with a '#' symbol.
# ■ It can have 3 or 6 digits.
# ■ Each digit is in the range of 0 to F. (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and F).
# ■ A - F letters can be lower case. (a,b,c,d,e and f are also valid digits).

# Examples

# Valid Hex Color Codes
# #FFF 
# #025 
# #F0A1FB 

# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff
import re

# to avoid matching on selectors, must be preceded by colon or space
pattern = r'(?<=[:\s])#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b'

N = int(input())

for i in range(N):
    # print(input())
    
    matched = re.findall(pattern, input())
    
    if matched:
        for i in matched:
            print(i)
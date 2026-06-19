# You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

# Input Format

# A single line of input containing a string of Roman characters.

# Output Format
# 
# Output a single line containing True or False according to the instructions above.
# 
# Constraints
# 
# The number will be between 1 and 3999 (both included).

regex_pattern = r"^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	
# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

# ^ and $ — Anchors matching the exact beginning and end of the string.
# (?=[MDCLXVI]) — A positive lookahead requiring at least one valid character so empty strings fail.
# M{0,3} — Matches the thousands place (0 to 3,000).
# (CM|CD|D?C{0,3}) — Matches the hundreds place: 900 (CM), 400 (CD), or 0–300/500–800 (D?C{0,3}).
# (XC|XL|L?X{0,3}) — Matches the tens place: 90 (XC), 40 (XL), or 0–30/50–80 (L?X{0,3}).
# (IX|IV|V?I{0,3}) — Matches the units place: 9 (IX), 4 (IV), or 0–3/5–8 (V?I{0,3}).
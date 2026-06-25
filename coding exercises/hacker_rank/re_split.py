# [] create a character class (a set of characters)
# within the brackets means match a character that is . and ,
# inside a character class the period loses its special match-any-character meaning

regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
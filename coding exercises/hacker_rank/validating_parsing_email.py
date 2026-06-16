# A valid email address meets the following criteria:

#     It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
#     The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
#     The domain and extension contain only English alphabetical characters.
#     The extension is , , or characters in length.

# Given pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

import re
import email.utils

N = int(input())

# for i in range(N):
#     orig = input()
    
#     p = orig.split()
    
#     # print(f"p: {p}")
    
#     # split by @ so username and domain first
#     # not splitting all at once for splitting by @ and . wont account
#     # for usernames with . eg test.test
#     username, domain = p[1].replace("<", "").replace(">", "").split('@', 1)
    
#     # print(username)
#     # print(domain)
    
#     # split domain and ext rsplit() starts from right, split() starts from left
#     domain_part, extension = domain.rsplit('.', 1)
    
    
#     # check username
#     pattern = r"^[a-zA-Z][a-zA-Z0-9_-]*$"
#     if re.match(pattern, username) == False:
#         continue
    
#     # check extension
#     if 1 <= len(extension) <= 3:
#         pass
#     else:
#         continue


pattern = r"[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}"
for _ in range(N):
    mail = email.utils.parseaddr(input())
    if re.fullmatch(pattern, mail[1]):
        print(email.utils.formataddr((mail[0], mail[1])))
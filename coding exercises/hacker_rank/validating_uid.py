# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.

# A valid UID must follow the rules below:

#     It must contain at least uppercase English alphabet characters.
#     It must contain at least digits ( - ).
#     It should only contain alphanumeric characters ( - , - & - ).
#     No character should repeat.
#     There must be exactly characters in a valid UID.

# Sample Input
# 2
# B1CD102354
# B1CDEF2354

# Sample Output
# Invalid
# Valid

# Enter your code here. Read input from STDIN. Print output to STDOUT

num = int(input())

# for i in range(num):
   
#     uid = input()
   
#     # check for at least 2 uppercase
#     twoupper = sum(c.isupper() for c in uid) >= 2
    
#     if twoupper == False:
#         print("Invalid")
#         continue
    
#     # check for at least 3 digits
#     threedigits = sum(c.isdigit() for c in uid) >= 3
    
#     if threedigits == False:
#         print("Invalid")
#         continue
        
#     # check if it only contain alphanumeric characters (a-z, A-Z & 0-9)
#     alphanum = uid.isalnum()
    
#     if alphanum == False:
#         print("Invalid")
#         continue
    
#     # check if no characters repeat
#     repeats = len(uid) == len(set(uid))
    
#     if repeats == False:
#         print("Invalid")
#         continue

#     # check for exactly 10 chars
#     if len(uid) == 10:
#         print ("Valid")
    

def run_checks(uid):
    return (
        len(uid) == 10 and
        uid.isalnum() and
        sum(c.isupper() for c in uid) >= 2 and
        sum(c.isdigit() for c in uid) >= 3 and
        len(uid) == len(set(uid))
    )
    
for i in range(num):
    ans = run_checks(input())
    
    if ans == True:
        print("Valid")
    else:
        print("Invalid")
    
    
    
    
    
    
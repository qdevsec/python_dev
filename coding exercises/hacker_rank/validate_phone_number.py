# A valid mobile number is a ten digit number starting with a 7, 8 or 9. 
import re

N = int(input())

for i in range(N):
    
    print("YES" if bool(re.match(r'^[789]\d{9}$', input())) else "NO")

# Enter your code here. Read input from STDIN. Print output to STDOUT

xk = list(map(int, input().split()))

# print(xk)

pf = input()

# print(pf)

x = xk[0]

ans = eval(pf)

# print(ans)

if ans == xk[1]:
    print(True)
else:
    print(False)
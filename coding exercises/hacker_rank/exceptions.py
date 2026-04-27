### Exceptions
# ZeroDivisionError - raised when the 2nd arg of a division of modulo operation is zero
# ValueError - when built in operation or function receives an argument that has
# has the right type but an inappropriate value

num_of_cases = int(input())


# use # of cases to set range
for i in range(0, num_of_cases):
    # place values in cases in a list
    ans = input().split()
    
    b = []
    # convert only numbers to int type
    for a in ans:
        
        try:
            b.append(int(a))
        except ValueError as e:
            print("Error Code:",e)
            b.append(a)
            pass
            
    # print(b)
    
    if isinstance(b[0], int) and isinstance(b[1], int):
        try:
            print(int(b[0] / b[1]))
        except ValueError as e:
            print("Error Code:",e)
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")


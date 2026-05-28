# Like most other programming languages, Python has the concept of closures. Extending these 
# closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def wrapper(f):
    def fun(l):
        
        a = []
        
        for i in range(len(l)):
            
            prefix = "+" + l[i][:-10]
            middle = l[i][-10:-5]
            suffix = l[i][-5:]
            
            if prefix == "+" or prefix == "+0" or prefix == "++91":
                prefix = "+91"
            
            num = " ".join(filter(None, [prefix, middle, suffix]))
            
            
            a.append(num)
        # complete the function
        
        f(a)
        
        # print(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
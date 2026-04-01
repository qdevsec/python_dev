import json

def reverse_list(the_list: list) -> list:
    
    r = (the_list)[::-1]
    print(r)
    
    # python reverse function, memory efficient
    # the_list.reverse()

    # [start:stop:step] [::-1] creates a shallow copy
    # when start is blank python defaults to the end 
    # when stop is blank python defaults to the beginning
    # the -1 says to move backward 1 element at a time 
    

def reverse_string(phrase: str) -> str:
    p = phrase
    r_word = ''
    the_list = list(phrase)

    for i in p:
        r_word = i + r_word

    print(r_word)

def start():
    print("starting....")
    ans = input("What do you want to reverse?: ")
    # print(ans.find('['))
    
    if ans.find('[') != -1:
        # print(ans)
        cleaned = [int(i) for i in ans.strip("[]").split(",")]
        reverse_list(cleaned)
    else:
        reverse_string(ans)

# start
start()
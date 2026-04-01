import re

file_path = "access.log"
pattern = r'401'

data =[]

def crude_parser(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            check = re.search(pattern, line)
            # print(check)
            if check:
                # print(line)
                data.append(line)

    print(data)
    return data

def find_stuff(data):
    print(data)
    
    for i in data:
        print(i)
        

find_stuff(crude_parser(file_path))
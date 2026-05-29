# You are given a valid XML document and you have to print the maximum level of nesting in it. Take the dept of the root as 0
# 
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    # your code goes here
    maxdepth = max(maxdepth,level)
    for i in elem:
        depth(i, level)
    

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
# You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of 
# each element. For any element, the score is equal to the number of attributes it has.

# sample input
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>

# Sample output
# 5

# There may be any level of nesting in the XML document. To learn about XML parsing, refer here.
# http://www.diveintopython3.net/xml.html
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    return sum(len(elem.attrib) for elem in node.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
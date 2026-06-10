#  You are given an HTML code snippet of N lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.

# Print the detected items in the following format:

# Print the detected items in the following format
# Tag1
# Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Tag3
# -> Attribute3[0] > Attribute_value3[0]
from html.parser import HTMLParser

class thehtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs) != 0:
            for name, value in attrs:
                print(f"-> {name} > {value}")

n = int(input())
html = '\n'.join(input() for i in range(n))

# create object from my class
parser = thehtmlparser()

# feed html data to parser
parser.feed(html)
parser.close()
# HTML
# Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

# Parsing
# Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.

# HTMLParser
# An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered. 

# .handle_starttag(tag, attrs)

# This method is called to handle the start tag of an element. (For example: <div class='marks'>)
# The tag argument is the name of the tag converted to lowercase.
# The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.

# .handle_endtag(tag)

# This method is called to handle the end tag of an element. (For example: </div>)
# The tag argument is the name of the tag converted to lowercase.

# .handle_startendtag(tag,attrs)

# This method is called to handle the empty tag of an element. (For example: <br />)
# The tag argument is the name of the tag converted to lowercase.
# The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def print_attrs(self,attrs):
        for name,value in attrs:
            print(f"-> {name} > {value if value is not None else 'None'}")

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            # attr[0] is the name, attr[1] is the value (which can be None)
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

    def handle_endtag(self, tag):
        print("End   :", tag)
    
    def handle_comment(self, data):
        pass

    # def handle_data(self, data):
    #     print("Encountered some data  :", data)

n = int(input())
html = '\n'.join(input() for i in range(n))
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Start : body
# -> data-modal-target > None
# -> class > 1
# Start : h1
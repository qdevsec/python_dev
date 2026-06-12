# .handle_comment(data)
# This method is called when a comment is encountered (e.g. <!--comment-->).
# The data argument is the content inside the comment tag:

# from html.parser import HTMLParserr

# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#           print("Comment  :", data)


# .handle_data(data)
# This method is called to process arbitrary data (e.g. text nodes and the content of <script>...</script> and <style>...</style>).
# The data argument is the text content of HTML.

# from html.parser import HTMLParserr

# class MyHTMLParser(HTMLParser):
#     def handle_data(self, data):
#         print("Data     :", data)
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print(">>> Multi-line Comment" if '\n' in data else ">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(f">>> Data\n{data}")
        # print(data)

# html = '\n'.join(input() for i in range(int(input())))

html = ""

for i in range(int(input())):
     html += input().rstrip()
     html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
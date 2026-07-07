# The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression. 
# The expression can be a Python statement, or a code object. 

# Here, eval() can also be used to work with Python keywords or defined functions and variables. 
# These would normally be stored as strings. 

# >>> type(eval("len"))
# <type 'builtin_function_or_method'>

# Without eval()

# >>> type("len")
# <type 'str'>

# Task
# You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).

eval(input())
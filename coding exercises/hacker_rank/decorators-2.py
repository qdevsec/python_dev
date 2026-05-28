# Using decorators to build a name directory
# Given some information about N people
# Each person has a first name, last name, age and sex
# Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first
# For two people of the same age, print them in the order of their input\
#
# Decorators are functions that extend the behavior of a base function w/o modifying the base function
# Pass the base function as an argument to the decorator
# if the base takes arguments then the wrapper function of the decorator should have *args, **kwargs
#
# def add_sprinkles(func):
#   def wrapper(*args, **kwargs):
#       print("*You add sprinkles*")
#       func(*args, **kwargs)
#   return wrapper
#
# @add_sprinkles
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream")

# get_ice_cream("vanilla")
#
# Output:
# You add sprinkles
# Here is your vanilla ice cream
import operator

def person_lister(f):
    def inner(people):
        a = []
        # need to convert the ages to a number so we sort by ints instead of
        # a string because alphabetically '10' is before '2'
        sort_it = sorted(people, key = lambda x : int(x[2]))
        # print(sort_it)
        # complete the function
        for i in range(len(sort_it)):
            a.append(f(sort_it[i]))
            
        return a

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

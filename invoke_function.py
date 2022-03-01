import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

def zero_arg_function():
    print("Invoking zero arg function")
print(zero_arg_function)
    


print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

def zero_arg_function():
    print("Invoking zero arg function")
print(zero_arg_function)


def introduction_with_default_args(first_name = "Courtny", last_name = "Robinson"):
    print("Hi, my name is %s %s" % first_name, last_name)
print(introduction_with_default_args (first_name= 'Courtny', last_name= 'Robinson'))
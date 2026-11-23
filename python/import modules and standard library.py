# when we import file, it runs all of the code from the module it imports
# that means all the print statements will also be executed
# if the module is in the same directory, we can import it directly
# import my_module 
import my_module as mm  # we would be using alias to make the module name shorter

courses = ["History", "Math", "Physics"]

# cannot directly call the find_index function
# we have to type the module name and then the function which we want to use
index = mm.find_index(courses, "Math")
print(index)
print(mm.test)



# importing a specific function
from my_module import find_index, test

# from my_module import find_index as fi, test # this works as well 
# to import everything 
# from my_module import * - frowned upon as it makes harder to track the functions

# since find_index and test was imported directly from my_module we can use this function directly
# if we use the function_name directly without specifically importing it, python will throw an error
index = find_index(courses, "Physics")
print(index)
print(test)



# built-in library that provides direct access to variables and functions maintained by the Python interpreter
import sys

# It is a list that contains the directory paths Python searches when executing an import statement. 
print(sys.path)

# You can append new folder paths to this list at runtime to import custom modules from other locations.
# sys.path is a list we can use append method to add any other directory
# sys.path.append("")

# we can also add new directories in the sys.path list by creating a new environment variables
# variable name = PYTHONPATH
# variable value =  (directory)

# some modules from standard library
import calendar
import datetime
import math
import os  # operating system
import random

random_course = random.choice(courses)

rads = math.radians(90)
math.sin(rads)

today = datetime.date.today()

calendar.isleap(2017)

print(os.getcwd()) #cwd - current working directory

# Dunder methods (short for "double underscore" methods, also known as magic methods) 
# Special built-in methods in Python that start and end with two underscores
print(os.__file__)  


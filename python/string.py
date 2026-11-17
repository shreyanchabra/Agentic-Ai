# This is a simple Python script that demonstrates how to create and print string variables using double quotes.
message = "Hello, World!"
print(message)

# This is a simple Python script that demonstrates how to create string variables using single quotes.
new_message = 'Hello, Python!'

# This is a simple Python script that demonstrates how to use single quotes as a character in a string variable.
third_message = "Shreyan's World"

# fourth_message = 'Shreyan's World'  # This line will cause a syntax error because of the unescaped single quote.
# To fix this, you can escape the single quote with a backslash
fourth_message = 'Shreyan\'s World'

multi_line_message = """This is a multi-line string.
It can span multiple lines without the need for escape characters."""

multi_line_message_2 = '''This is a multi-line string with single quotes.
It can span multiple lines without the need for escape characters.'''

# This is a simple Python script that demonstrates how to use the len() function to get the length of a string variable.
print(len(message))  # Output: 13
print(len(multi_line_message))  # Output: 56

# This is a simple Python script that demonstrates how to access individual characters in a string variable using indexing.
print(message[0])  # Output: H
print(message[7])  # Output: W

# This is a simple Python script that demonstrates how to access individual characters in a string variable using negative indexing.
print(message[-1])  # Output: !
print(message[-2])  # Output: d

# This is a simple Python script that demonstrates how to use slicing to access a range of characters in a string variable.
# First index is inclusive and second index is exclusive
print(message[0:5])  # Output: Hello
# If you omit the first index, it defaults to 0
print(message[:5])  # Output: Hello
# If you omit the second index, it defaults to the length of the string
print(message[7:])  # Output: World!

# Difference between methods and functions in python
# A function is a block of code that performs a specific task and can be called by its name. 
# It can take input arguments and return output values. Functions are defined using the def keyword. 
# A method is a function that is associated with an object. 
# It can be called on an instance of a class and has access to the object's data and methods. 
# Methods are defined within a class and are called using the dot notation.


# count() method is used to count the number of occurrences of a substring in a string.
# We can use both single and double quotes to define a string in Python.
# Python doesn't have the concept of character data type, it treats a single character as a string of length 1.
print(message.count("o"))  # Output: 2
print(message.count("Hello"))  # Output: 1
print(message.count("Python"))  # Output: 0

# find() method is used to find the index of the first occurrence of a substring in a string.
# If the substring is not found, it returns -1.
print(message.find("World"))  # Output: 7
print(message.find("Universe"))  # Output: -1


# The below methods do not modify the original string, they return a new string with the modifications.
# lower() method is used to convert all the characters in a string to lowercase.
print(message.lower())  # Output: hello, world!

# upper() method is used to convert all the characters in a string to uppercase.
print(message.upper())  # Output: HELLO, WORLD!

# replace() method is used to replace all occurrences of a substring in a string with another substring.
# first argument is the substring to be replaced and the second argument is the substring to replace with.
print(message.replace("World", "Universe"))  # Output: Hello, Universe!


# To store the modified string in a new variable, we can do the following:
modify_message = message.replace("World", "Universe")
print(modify_message)  # Output: Hello, Universe!


# Concatenation of strings
greeting = "Hello"
name = "Shreyan"
# We can concatenate strings using the + operator.  
greeting_message = greeting + ", " + name + "!"
print(greeting_message)  # Output: Hello, Shreyan!  

# format() method is used to format strings by replacing placeholders with values.
# greeting_message_2 = "{}, {}! Welcome to Python.".format(greeting, name) ## Use f-string instead of `format` call

# formatting strings using f-strings (formatted string literals)
# add an 'f' before the single/double quotes and use curly braces {} to include variables or expressions inside the string.
# greeting_message_2 = f'{greeting}, {name}! Welcome to Python.'
greeting_message_2 = f"{greeting}, {name}! Welcome to Python."

# we can also use methods/expressions inside the curly braces
print(f"{greeting}, {name.upper()}! Welcome to Python.") # Output: Hello, SHREYAN! Welcome to Python.

# dir() method is used to get a list of all the attributes and methods of an object.
print(dir(name))

# help() method is used to get the documentation of an object.
# help() takes "data type" as an argument.
print(help(str))

# to get the documentation of a specific method on a data type, we can use the following syntax:
print(help(str.lower)) 

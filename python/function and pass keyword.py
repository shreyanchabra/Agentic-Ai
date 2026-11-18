# def keyword. Signals to Python that you are creating a new function.
# Function name. Follows the same naming rules as variables (lowercase with underscores is standard).
# Parameters. Optional input variables listed inside parentheses.
# Colon (:). Marks the end of the function header.
# Indented body. The code that runs when the function is called. Python requires consistent indentation (usually 4 spaces).
def hello_function():
    return "Hello Function"


# pass is a null operation that acts as a placeholder when a statement is syntactically required, but no code needs to execute
# common use cases of pass
# empty functions and methods
def process_data():
    pass


# empty classes and custom exceptions
class CustomError(Exception):
    pass


# conditional statements
x = 5
if x > 10:
    pass  # Intentionally do nothing
else:
    print("x is 10 or less")

# loops
for i in range(5):
    if i == 3:
        pass
    print(i)


# common examples of def
# simple functions (No Parameters)
def greet():
    print("Hello, welcome to Python!")


greet()


# function with parameters and a return value
def add_numbers(a, b):
    """ Returns the sum of two numbers """ 
    """ This is called doc strings """
    total = a + b
    return total


result = add_numbers(5, 3)
print(result)  # Output: 8


# default parameter values
def welcome_user(name="Guest"):
    print(f"Welcome, {name}!")


welcome_user("Alex")  # Output: Welcome, Alex!
welcome_user()  # Output: Welcome, Guest!

# Parameter without a default cannot follow a parameter with a default
# def sum(int_1, int_2 = 5, int_3) # error


# If you write greet without parentheses, the function does not run.
# Instead, Python simply looks up the function object in memory and does nothing with it, producing no error and no output.
# greet

# Writing greet prints the function's memory reference, instead of running the code inside it.
print(greet)  # Output: <function greet at 0x0000019DB1257ED0>

# We can treat the executed function just as the data type it returns and chain methods on it
print(hello_function().upper())  # Output: HELLO FUNCTION


# *args and **kwargs allow functions to accept a variable number of arguments
# *args
def add_numbers(*args):  # 'args' is a tuple containing all passed numbers
    return sum(args)


print(add_numbers(5, 10))  # Output: 15
print(add_numbers(1, 2, 3, 4))  # Output: 10


# **kwargs
def print_profile(**kwargs):  # 'kwargs' is a dictionary of key-value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Alice", role="Developer", city="New York")

# When combining standard parameters with *args and **kwargs, you must follow a strict sequence.
# Standard parameters come first, followed by *args, and **kwargs must always be last

## args and kwargs are only conventions.
## The asterisks (* and **) do the actual work, so names like *numbers or **options are completely valid.


def student_info(*args, **kwargs):
    print(args) # args is a tuple
    print(kwargs) # kwargs is a dictionary

student_info("Maths", "Art", name="John", age=22)

courses = ['Maths', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info) # Output: (['Maths', 'Art'], {'name': 'John', 'age': 22}) - positional arguments
                            # Output: {} - keyword arguments
                            # not what we intended

student_info(*courses, **info) # Output: ('Maths', 'Art') 
                               # Output: {'name': 'John', 'age': 22}
                               # unpacked as intended




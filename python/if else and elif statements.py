# boolean values in python are True and False (T and F uppercase)

if True:
    print("Condition was True")

if False:
    print("Condition was False")

language = "Python"

# if
if language == "Python":
    print("Language is Python")


# else
if language == "Python":
    print("Language is Python")
else:
    print("No match")


# elif
if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("No match")

## no concept of switch statements in Python


# boolean operators - and, or and not
user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("Admin Page")  # Output
else:
    print("Check credentials")


user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Check credentials")  # Output


if user == "Admin" or logged_in:
    print("Admin Page")  # Output
else:
    print("Check credentials")


if not logged_in:
    print("Please log in")  # Output
else:
    print("Welcome")


# object identity
# id() method returns a unique integer identifying an object in memory
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = list_1

print(id(list_1))  # Output: 1431625464960
print(id(list_2))  # Output: 1431627072768
print(id(list_3))  # Output: 1431625464960 - same as list_1

# is Operator
# tests if two objects has the same id i.e. both references the exact same object in memory.
# compares the memory identities of two variables rather than their data values.

print(list_1 == list_2)  # Output: True
print(list_1 is list_2)  # Output: False
print(list_1 is list_3)  # Output: True


# False Values in Python
# False
# None
# Zero of any numeric type. For example: 0, 0.0
# Any empty sequence. For example: "", (), []
# Any empty mapping. For example: {}


# unlike Java, Python supports chained comparison operators
month = 2
if 1 <= month <= 12:
    print("Valid month")

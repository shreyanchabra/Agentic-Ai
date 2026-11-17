num = 3
print(type(num))  # Output: <class 'int'>

num_float = 3.14
print(type(num_float))  # Output: <class 'float'>

# type() method is used to get the data type of a variable.

print(3 + 2) # Output: 5 - addition
print(3 - 2) # Output: 1 - difference
print(3 * 2) # Output: 6 - multiplication
print(3 / 2) # Output: 1.5 - proper division 
print(3 // 2) # Output: 1 - floor division
print(3 ** 2) # Output: 9 - exponentiation
print(3 % 2) # Output: 1 - modulus

# order of operations in Python follows the BODMAS rule (Brackets, Order, Division and Multiplication, Addition and Subtraction).
print(3 + 2 * 2) # Output: 7 - multiplication is done first
print((3 + 2) * 2) # Output: 10 - brackets are done first 
print(3 + 2 ** 2) # Output: 7 - exponentiation is done first
print((3 + 2) ** 2) # Output: 25 - brackets are done first

# increment and decrement operators are not available in Python. 
# Instead, we can use the += and -= operators to increment and decrement a variable.
num += 1  # Equivalent to num = num + 1
num -= 1  # Equivalent to num = num - 1

# we can also use the *= and /= operators to multiply and divide a variable by a certain value.
num *= 2  # Equivalent to num = num * 2
num /= 2  # Equivalent to num = num / 2

# abs() method is used to get the absolute value of a number.
print(abs(-3)) # Output: 3

# round() method is used to round a number to a certain number of decimal places.
print(round(3.14159, 2)) # Output: 3.14
# if the second argument is not provided, it rounds to the nearest integer.
print(round(3.14159)) # Output: 3

# Comparison operators are used to compare two values and return a boolean value (True or False).
num_1 = 3
num_2 = 2  
print(num_1 > num_2)  # Output: True
print(num_1 < num_2)  # Output: False
print(num_1 == num_2) # Output: False
print(num_1 != num_2) # Output: True
print(num_1 >= num_2) # Output: True
print(num_1 <= num_2) # Output: False

num_3 = "100"
num_4 = "200"
print(num_3 > num_4)  # Output: False - because string comparison is done lexicographically
print(num_3 + num_4)  # Output: "100200" - instead of adding the numbers, it concatenates the strings

# to convert a string to a number, we can use the int() or float() methods - cast the string to an integer or float respectively.
num_3 = int(num_3)
num_4 = int(num_4)
print(num_3 + num_4)  # Output: 300 - now the strings are converted to integers and added together
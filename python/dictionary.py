student = {
    "name": "John",
    "age": 21,
    "courses": ["Computer Science", "Mathematics", "Physics"]
}

print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Computer Science', 'Mathematics', 'Physics']}
print(student["name"])  # Output: John
print(student["age"])  # Output: 21
print(student["courses"])  # Output: ['Computer Science', 'Mathematics', 'Physics']

# key can be any immutable type, such as strings, numbers, or tuples
# dictionary with mixed key types
mixed_dict = {
    "name": "Alice",
    42: "The answer to life, the universe, and everything",
    (1, 2): "A tuple as a key"
}

print(mixed_dict)  # Output: {'name': 'Alice', 42: 'The answer to life, the universe, and everything', (1, 2): 'A tuple as a key'} 
print(mixed_dict["name"])  # Output: Alice
print(mixed_dict[42])  # Output: The answer to life, the universe, and everything
print(mixed_dict[(1, 2)])  # Output: A tuple as a key

# accessing keys which do not exist in the dictionary
# print(student["address"])  # This will raise a KeyError

# Using the get() method to access keys that may not exist
print(student.get("address"))  # Output: None
print(student.get("address", "Not found"))  # Output: Not found - default value if key does not exist
print(student.get("name"))  # Output: John

# adding new key-value pairs to the dictionary
student["address"] = "123 Main St"

# if the key already exists, it will update the value
student["age"] = 22

print(student)  # Output: {'name': 'John', 'age': 22, 'courses': ['Computer Science', 'Mathematics', 'Physics'], 'address': '123 Main St'}

# adding/updating multiple key-value pairs using the update() method
    # if the key already exists, it will update the value; if the key does not exist, it will add a new key-value pair
    # update() method takes a dictionary as an argument
student.update({"age": 23, "email": "john@example.com"})

print(student)  # Output: {'name': 'John', 'age': 23, 'courses': ['Computer Science', 'Mathematics', 'Physics'], 'address': '123 Main St', 'email': 'john@example.com'}

# deleting key-value pairs from the dictionary
del student["address"]
print(student)  # Output: {'name': 'John', 'age': 23, 'courses': ['Computer Science', 'Mathematics', 'Physics'], 'email': 'john@example.com'}

# pop() method removes the specified key and returns the corresponding value
age = student.pop("age")    
print(age)  # Output: 23
print(student)  # Output: {'name': 'John', 'courses': ['Computer Science', 'Mathematics', 'Physics'], 'email': 'john@example.com'}  

# len() method returns the number of keys in the dictionary
print(len(student)) 

# keys(), values() and items() method returns the list of keys, list of values and list of key-value pair as a tuple respectively
print(student.keys())
print(student.values())
print(student.items())

# using for loop to access key, value and key-value pair
for key in student:
    print(key)

# for key in student.keys(): ## keys can also be looped from student.keys() list
    # print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)
    print(f"{key}: {value}")
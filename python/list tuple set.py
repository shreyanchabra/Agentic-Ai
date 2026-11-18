# lists in Python

courses = ["Python", "Java", "C++", "JavaScript"]
print(courses)  # Output: ['Python', 'Java', 'C++', 'JavaScript']

# len() method is used to get the length of a list.
print(len(courses))  # Output: 4

# accessing elements in a list using index
print(courses[0])  # Output: 'Python'
print(courses[2])  # Output: 'C++'
print(courses[-1])  # Output: 'JavaScript' - accessing the last element

# slicing a list to get a sublist
# first index is inclusive and second index is exclusive
print(courses[1:3])  # Output: ['Java', 'C++']
# if you omit the first index, it defaults to 0
print(courses[:2])  # Output: ['Python', 'Java']
# if you omit the second index, it defaults to the length of the list
print(courses[2:])  # Output: ['C++', 'JavaScript']


# list methods

# append() method is used to add an element to the end of a list.
courses.append("Go")
print(courses)  # Output: ['Python', 'Java', 'C++', 'JavaScript', 'Go']

# insert() method is used to add an element at a specific index in a list.
# first argument is the index where the element should be added and the second argument is the element to be added.
courses.insert(1, "Ruby")
print(courses)  # Output: ['Python', 'Ruby', 'Java', 'C++', 'JavaScript', 'Go']

# extend() method is used to add multiple elements to the end of a list.
# second argument is an iterable (list, tuple, set, etc.) whose elements will be added to the list.
courses.extend(["PHP", "Swift"])
print(
    courses
)  # Output: ['Python', 'Ruby', 'Java', 'C++', 'JavaScript', 'Go', 'PHP', 'Swift']

# remove() method is used to remove the first occurrence of an element from a list.
courses.remove("C++")
print(courses)  # Output: ['Python', 'Ruby', 'Java', 'JavaScript', 'Go', 'PHP', 'Swift']

# pop() method is used to remove an element from a list at a specific index and return the removed element.
# If no index is specified, it removes and returns the last element of the list.
print(courses.pop(2))  # Output: 'Java' - removes and returns the element at index 2
print(courses.pop())  # Output: 'Swift' - removes and returns the last element
print(courses)  # Output: ['Python', 'Ruby', 'JavaScript', 'Go', 'PHP']

# reverse() method is used to reverse the order of elements in a list.
courses.reverse()
print(courses)  # Output: ['PHP', 'Go', 'JavaScript' , 'Ruby', 'Python']

# sort() method is used to sort the strings alphabetically.
courses.sort()
print(courses)  # Output: ['Go', 'JavaScript', 'PHP', 'Python', 'Ruby']

# sort() method is used to sort the numbers in ascending order.
numbers = [3, 1, 4, 2, 5]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 5]

# sorting in descending order can be done by passing the reverse=True argument to the sort() method.
numbers.sort(reverse=True)
print(numbers)  # Output: [5, 4, 3, 2, 1]

# sorted() method is used to sort a list without modifying the original list.
numbers = [3, 1, 4, 2, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]
print(numbers)  # Output: [3, 1, 4, 2, 5]

# min(), max() and sum() methods
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 5
print(sum(numbers))  # Output: 15

# min(), max() and sum() methods on a list of strings
print(min(courses))  # Output: Go
print(max(courses))  # Output: Ruby
# print(sum(courses))  # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str' - sum() cannot be used on a list of strings

# index() method is used to get the index of the first occurrence of an element in a list.
print(courses.index("PHP"))  # Output: 0
# print(courses.index("Java")) # Output: ValueError: 'Java' is not in list - raises an error if the element is not found in the list

# To check if an element is present in a list, we can use the 'in' keyword.
print("Python" in courses)  # Output: True
print("Java" in courses)  # Output: False

# for loop can be used to iterate over each elements of a list.
for course in courses:
    print(course)

# enumerate() method is used to get the index and value of each element in a list.
for index, course in enumerate(courses):
    print(index, course)

# start argument can be passed to the enumerate() method to start the index from a specific number.
for index, course in enumerate(courses, start=1):
    print(index, course) 

# join() method is used to join the elements of a list into a single string.
# The join() method takes a string as an argument and joins the elements of the list using that string as a separator.
courses_str = "-".join(courses)
print(courses_str)  # Output: Go-JavaScript-PHP-Python-Ruby

# split() method is used to split a string into a list of substrings.
courses_list = courses_str.split("-")
print(courses_list)  # Output: ['Go', 'JavaScript', 'PHP', 'Python', 'Ruby']   



# tuples in Python

# Lists are mutable, meaning their elements can be changed, added, or removed. 
# Tuples, on the other hand, are immutable, meaning their elements cannot be changed once they are created.
# Tuples are defined using parentheses () instead of square brackets [].
courses_tuple = ("Python", "Java", "C++", "JavaScript")
print(courses_tuple)  # Output: ('Python', 'Java', 'C++', 'JavaScript')



# sets in Python

# Sets are unordered collections of unique elements.
# Sets are mutable
# Sets do not allow duplicate elements
# Sets are defined using curly braces {}.
courses_set = {"Python", "Java", "C++", "JavaScript"}   
print(courses_set)  # Output: {'Java', 'C++', 'Python', 'JavaScript'} - the order of elements may vary

print("Python" in courses_set)  # Output: True - optimal for membership testing

# comparing two sets using set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union() method is used to get the union of two sets.
set_union = set1.union(set2)
print(set_union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# intersection() method is used to get the intersection of two sets.
set_intersection = set1.intersection(set2)
print(set_intersection)  # Output: {4, 5}

# difference() method is used to get the difference of two sets.
set_difference = set1.difference(set2)  
print(set_difference)  # Output: {1, 2, 3} - elements in set1 but not in set2




# creating empty list, tuple and set
empty_list = []
# empty_list = list()  # empty list can also be created using the list() constructor

empty_tuple = ()
# empty_tuple = tuple()  # empty tuple can also be created using the tuple() constructor

# empty set can only be created using the set() constructor, using {} creates an empty dictionary.
empty_set = {}  # This creates an empty dictionary, not a set
empty_set = set()  # empty set can also be created using the set() constructor


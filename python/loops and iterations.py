nums = [1, 2, 3, 4, 5]

# for loop
for num in nums:
    print(num)

# break keyword - completely break out of the loop
for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)

# continue keyword - move into the next iteration of the loop
for num in nums:
    if num == 3:
        print("Skip!")
        continue
    print(num)

# nested loops
for num in nums:
    for letter in "abc":
        print(num, letter)

# range()
# syntax: range(start, stop, step)
# start (optional). This is the first number in the sequence. It defaults to 0 if you leave it out.
# stop (required). The sequence generates numbers up to, but not including, this value.
# step (optional). This defines the difference between each number in the sequence. It defaults to 1 and cannot be zero.

for i in range(10):
    print(i)  # Outputs: 0,1,2,3,4,5,6,7,8,9

for i in range(5, 10):
    print(i)  # Outputs: 5,6,7,8,9

for i in range(1, 11, 2):
    print(i)  # Outputs: 1,3,5,7,9


# while loops
x = 0
while x < 10:
    print(x)
    x += 1

# infinte loop
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

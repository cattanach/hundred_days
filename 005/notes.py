# loops!

# assigning variable name fruit to each item in list
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit + " pie")

 #range

for number in range (1, 10): # not including 10
    print(number)

for number in range (1, 11, 3): # in steps of 3
    print(number)

print()

# the below is the factorial of 100

total = 0
for number in range(1, 101):
    total += number
print(total)


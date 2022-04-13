# code blocks, functions, while loops

print() # all funtions have parentheses

# define function

def my_function():
    print("hello")
    print("bye")

# call function

my_function()

# https://reeborg.ca/reeborg.html

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def turn_around():
#     turn_left()
#     turn_left()

# move()
# turn_left()
# move()
# turn_right()
# move()
# turn_around()


# while loops

def jump():
    print("JUMP")

for step in range(6):
    jump()

# OR

number_of_hurles = 6
while number_of_hurles > 0:
    jump()
    number_of_hurles -= 1
    print(number_of_hurles)

# this'll run once

something_is_true = True

while something_is_true:
    print("do this")
    something_is_true = False

# for loops are good for iterating through a sequence, like printing each item in a list
# while loops are good when for when you don't care how many things are in a sequence
# while loops are more dangerous cause they don't necessarily have a set end - infinite loop
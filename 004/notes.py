# randomisation
# https://khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators 

import random
import module_test

random_integer = random.randint(1,10)
print(random_integer)

# module = function? sorta

print(module_test.pi)

random_float = random.random()
print(random_float) # between 0.0 and 0.999999...
print(type(random_float))

# to get a random_float between 0 and 5:
random_float_between_0_and_5 = random_float * 5
print(random_float_between_0_and_5)

print(module_test.random_integer_test)

# lists
# data structure
# open and closed brackets with commas
# https://docs.python.org/3/tutorial/datastructures.html

states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas"]
print(states_of_america[0]) # this is alabama
print(states_of_america[-1]) # this is arkansas
print(states_of_america[random.randint(0,3)]) # who knowwwwwwwws

states_of_america[0] = "poop" # changes the value of item 0 
print(states_of_america)

states_of_america.append("Puerto Rico") # adds Puerto Rico to the Union
print(states_of_america)

states_of_america.extend(["Canada", "Mexico"]) # adds multiple items to the list. adding a list to a list essentially
print(states_of_america)

print(len(states_of_america))

# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
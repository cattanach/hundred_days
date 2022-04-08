# print(len(12345)) TypeError: object of type 'int' has no len()

print("Hello"[0]) # gets first character of string - subscript
"hello"[4]

print(123 + 456)
123_456_789 # more readable, same as 123,456,789
print (123_456_789) # returns 123456789

num_char = 6 # len(input("What is your name? "))
# print("Your name has " + num_char + " characters.") TypeError: can only concatenate str (not "int") to str

print(type(num_char)) # this returns: <class 'int'>

new_num_char = str(num_char) # casts num_char to string type
print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

70 + float("100.5") # returns 170.5, 70 is converted to float

# division always results in a float
# print(6/3) returns 2.0

# exponent is **
2 ** 3 # is 2 cubed

# order of operations P E MD AS l->r

# int removes all decimals without rounding:
print(8 / 3)
# this will round to 2 decimal places:
print(round(8 / 3, 2))
# floor division drops the decimals, converts to integer
print(8 // 3)
# modulooooooo
print(8 % 3)

# divide result by two again /=
result = 4 / 2
result /= 2
print(result)

score = 0 
score += 1
print(score)

# f-strings are tight, automatically converts other types to string

score = 0
height = 1.8
is_winning = True

print(f"your score is {score}, your height is {height} and you are winning is {is_winning}")

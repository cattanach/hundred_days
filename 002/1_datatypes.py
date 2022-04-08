# 🚨 Don't change the code below 👇
from tkinter import YView


two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# input is always a string, so this step is unnecessary
new_two_digit_number = str(two_digit_number)

first_digit = (new_two_digit_number)[0]
second_digit = (new_two_digit_number)[1]

# overly complicated way to do it:

a = int(first_digit)
b = int(second_digit)

total = a + b
str_total = str(total)

print(first_digit + " + " + second_digit + " = " + str_total)
print(str_total)

# much better way to do it:

result = int(first_digit) + int(second_digit)
print(result)
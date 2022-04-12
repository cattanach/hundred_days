#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

str_letters = ""
str_symbols = ""
str_numbers = ""
# could set password = "" instead and just add to that instead of these separate variables

for i in range (1, nr_letters + 1):
    str_letters += letters[random.randint(0,51)]
    # could do password += random.choice(letters)

for i in range (1, nr_symbols + 1):
    str_symbols += symbols[random.randint(0,8)]

for i in range (1, nr_numbers + 1):
    str_numbers += numbers[random.randint(0,9)]

easy_password = str_letters+str_symbols+str_numbers

print(easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# using google

hard_password = ''.join(random.sample(easy_password,len(easy_password)))

print(hard_password)

# from the lesson

password_list = []

for i in range (1, nr_letters + 1):
    password_list.append(random.choice(letters))

for i in range (1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for i in range (1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for character in password_list:
    password += character

print(password)
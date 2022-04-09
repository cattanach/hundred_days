# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

letter_t  = name1.count("t") + name2.count("t")
letter_r  = name1.count("r") + name2.count("r")
letter_u  = name1.count("u") + name2.count("u")
letter_e  = name1.count("e") + name2.count("e")
letter_l  = name1.count("l") + name2.count("l")
letter_o  = name1.count("o") + name2.count("o")
letter_v  = name1.count("v") + name2.count("v")
letter_e  = name1.count("e") + name2.count("e")

first_digit = letter_t + letter_r + letter_u + letter_e
second_digit = letter_l + letter_o + letter_v + letter_e

score = int(f"{first_digit}{second_digit}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

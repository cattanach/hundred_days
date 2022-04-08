# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

total_with_tip = bill + ((bill * tip) / 100)
# total_each = round(total_with_tip / people, 2) will only return to one decimal, eg = 1.70 shows 1.7
total_each = "{:.2f}".format(total_with_tip / people)

print(f"Each person should pay £{total_each}.")

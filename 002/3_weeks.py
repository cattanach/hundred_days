# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days = (90 * 365) - (int(age) * 365)
weeks = (90 * 52) - (int(age) * 52)
months = (90 * 12) - (int(age) * 12)

# -- OR --

age_as_int = int(age)
years_remaining = 90 - age_as_int

days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

# --------

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)
print("Welcome to the rollercoaster")
height = int(input("What is your hieght in cm? "))

if height >= 120:
    print("you can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("£5 plz")
    elif age <= 18:
        print("£7 plz")
    else:
        print("£12 plz")
else:
    print("bad luck shorty")


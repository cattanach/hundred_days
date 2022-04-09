print("Welcome to the rollercoaster")
height = int(input("What is your hieght in cm? "))
bill = 0

if height >= 120:
    print("you can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are £5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are £7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. Have a free ride on us!")
        bill = 0
    else:
        print("Adult tickets are £12.")
        bill = 12

    wants_photo = input("Do you want a photo? Y/N ")
    if wants_photo == "Y":
        # Add £3 to bill
        bill += 3

    print(f"Your bill is £{bill}")

else:
    print("bad luck shorty")


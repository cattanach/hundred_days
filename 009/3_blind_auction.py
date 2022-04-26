import os
def clear(): os.system('clear') #on Linux System

# beginning UI
from art import logo
print(logo)
print("FPSBA v1.0 (c) 2022")

# create dictionary
bids = {}

others = "y"
while others != "n":

    # get data
    name = input("What is your name? ")
    amount = int(input("How much do you bid? £"))
    others = input("Are there any other bidders? y/n ")

    # adds bids to dictionary
    bids[name] = amount

    #clear screen
    clear()

#find highest bidder
highest_bid = 0
highest_bidder = ""

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of £{highest_bid}.")
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
import os
from art import logo

def clear(): os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    
    keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if keep_playing == 'n':
        quit() 

    clear()

    player_hand = []
    dealer_hand = []

    print(logo)

    # deal cards

    def deal_card():
        return cards[random.randint(0,12)]

    player_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    dealer_hand.append(deal_card())

    # calculate scores

    def calculate_score(list_of_cards):
        if (sum(list_of_cards) > 21) and (11 in list_of_cards):
            list_of_cards.remove(11)
            list_of_cards.append(1)
            return(sum(list_of_cards))
        else:
            return(sum(list_of_cards))

    # flop display

    print(f"Your hand: {player_hand}, current total: {calculate_score(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    if calculate_score(dealer_hand) == 21 and calculate_score(player_hand) == 21:
        print(f"draw")
        blackjack()
    elif calculate_score(player_hand) == 21:
        print("Blackjack. You win.")
        blackjack()

    # player gameplay

    keep_playing = True
    
    while calculate_score(player_hand) < 21 and keep_playing == True:
        hit = input("Type 'y' to hit, or 'n' to stay: ")
        if hit == "y":
            player_hand.append(deal_card())
            print(f"Your hand: {player_hand}, current total: {calculate_score(player_hand)}")
            keep_playing = True
        elif hit == "n":
            keep_playing = False
        else:
            print("invalid input")

    # dealer gameplay

    while calculate_score(dealer_hand) < 17 and calculate_score(player_hand) < 22:
        dealer_hand.append(deal_card())

    # scoring

    def final_scores():
        print(f"Your final hand: {player_hand}, final total: {calculate_score(player_hand)}")
        print(f"Dealer's final hand: {dealer_hand}, final total: {calculate_score(dealer_hand)}")

    def calculate_winner(final_player_score,final_dealer_score):
        if final_player_score > 21 and final_dealer_score < 21:
            print("You went over. You lose.")
        elif final_dealer_score > 21 and final_player_score < 21:
            print("Dealer went over. You won.")
        elif final_player_score == final_dealer_score:
            print("It's a draw.")
        elif final_player_score == 21:
            print("You won.")
        elif final_player_score > final_dealer_score:
            print("You won.")
        elif final_player_score < final_dealer_score:
            print("You lost.")

    # results

    if keep_playing == False and calculate_score(player_hand) < 21:
        final_scores()
        calculate_winner(calculate_score(player_hand),calculate_score(dealer_hand))
        blackjack()
    elif calculate_score(player_hand) > 21:
        calculate_winner(calculate_score(player_hand),calculate_score(dealer_hand))
        final_scores()
        blackjack()
    elif calculate_score(player_hand) == 21:
        calculate_winner(calculate_score(player_hand),calculate_score(dealer_hand))
        final_scores()
        blackjack()
    
blackjack()
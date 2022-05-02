
import random
import os
from art import logo

def clear(): os.system('clear')

play_count = 0
win_count = 0

def game():

    global play_count
    global win_count

    answer = random.randint(1,100)

    print(logo)

    print("I'm thinking of a number between 1 and 100.\n ")
    # print(f"THE ANSWER IS {answer}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        guesses = 10
    elif difficulty == "hard":
        guesses = 5

    play = True

    while play and guesses != 0:
        print(f" \nYou have {guesses} attempts remaining to guess the number.")
        number = int(input("Make a guess: "))
        if number == answer:
            print(f" \nYou got it! The answer was {answer}.")
            win_count += 1
            play = False
        elif number != answer and guesses > 0:
            guesses -= 1
            if number > answer:
                print("Too high.")
            elif number < answer:
                print("Too low.")

    if guesses == 0:
        print(f" \nOut of guesses. The answer was {answer}.")
        play = False

    play_count += 1

    print(f" \nYou've won {win_count} out of {play_count} games.")
    keep_playing = input(" \nTry again? 'y' or 'n': ")
    if keep_playing != "n":
        clear()
        game()
    else:
        quit()

game()
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player = input("rock paper scissors shoot! \n").lower()
computer = random.randint(0,2)
images = [rock,paper,scissors]

if player != "rock" and player != "paper" and player != "scissors":
    print("invalid input")
else:
    if player == "rock":
        print(rock)
        player = 0
    elif player == "paper":
        print(paper)
        player = 1
    elif player == "scissors":
        print(scissors)
        player = 2

    print("\nthe computer played:")

    print(images[computer])

    if (player == 0 and computer == 2) or (player > computer):
        print("you won")
    elif (computer == 0 and player == 2) or (player < computer):
        print("you lost")
    elif player == computer:
        print("draw")
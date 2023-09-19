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

print("Welcome to Rock, Paper, Scissors!")
yourTurn = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
import random
computerTurn = random.randint(0,2)
if yourTurn == 0:
    print(rock)
    if computerTurn == 0:
        print(rock)
        print("It's a draw!")
    elif computerTurn == 1:
        print(paper)
        print("You lose!")
    else:
        print(scissors)
        print("You win!")

elif yourTurn == 1:
    print(paper)
    if computerTurn == 0:
        print(rock)
        print("You win!")
    elif computerTurn == 1:
        print(paper)
        print("It's a draw!")
    else:
        print(scissors)
        print("You lose!")

else:
    print(scissors)
    if computerTurn == 0:
        print(rock)
        print("You lose!")
    elif computerTurn == 1:
        print(paper)
        print("You win!")
    else:
        print(scissors)
        print("It's a draw!")

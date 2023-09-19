from art import logo
from game_data import data
import random
import os

#format account data
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_ans(guess, a_follower, b_follower):
    if a_follower>b_follower:
        return guess=="a"
    else:
        return guess=="b"

score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    #random account
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Aginst B: {format_data(account_b)}.")

    #ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ")

    #follower count
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_ans(guess, a_follower_count, b_follower_count)
    os.system('cls')
    #give feedback
    if is_correct:
        score +=1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry! that's wrong. Final score: {score}")
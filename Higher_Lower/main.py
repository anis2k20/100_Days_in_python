import random
from game_data import data
from art import logo
#print(logo)

game_should_continue = True

while game_should_continue:
    random_num1 = random.randint(0,50)
    random_num2 = random.randint(0,50)
    #Random Account
    def random_account(rand_num,data):
        rand_acc = data[rand_num]
        print(f"Compare A: {rand_acc['name']}, a {rand_acc['description']}, from {rand_acc['country']}")
        followers = rand_acc["follower_count"]
        return followers

    #random account for user
    def random_account_user(rand_num,data):
        rand_acc = data[rand_num]
        print(f"Against B: {rand_acc['name']}, a {rand_acc['description']}, from {rand_acc['country']}")
        followers = rand_acc["follower_count"]
        return followers

    f1 = random_account(random_num1,data)
    f2 = random_account_user(random_num2,data)
    computer_big=f1
    print(f1)
    print(f2)

    def compare(f1,big,f2):
        score=0
        if f1==big and f2>big:
            print("You lose")
            game_should_continue = False
        elif f1==big and f2<big:
            print("Correct.")
            score +=1

        elif big>f1:
            print("Correct.")
            score+=1

        elif big<f1:
            print("You lose")
            game_should_continue = False
        print(f"Your score is {score}")

    def user_input(f1,f2):
        guess = input("Who is bigger? Type 'A' or 'B': ").lower()
        if guess == "a":
            return f1
        elif guess =="b":
            return f2

    big=user_input(f1,f2)
    print(f"big is {big}")

    print(f"f1: {computer_big},big: {big}")
    compare(computer_big,big,f2)





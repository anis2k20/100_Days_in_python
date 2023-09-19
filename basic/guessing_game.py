from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def game():
    answer = randint(1, 100)

    # compare function--------------------
    def check_ans(guess, ans, turns):
        if guess > ans:
            print("Too high")
            return turns - 1
        elif guess < ans:
            print("Too low")
            return turns - 1
        else:
            print(f"You got it!. The answer was {ans}")

    # end compare----------------------------

    # level set function --------------
    def level_set():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURNS
            # print(f"You have {EASY_LEVEL_TURNS} attempts remaining to guess the number.")
        else:
            return HARD_LEVEL_TURNS

    print("Welcome to the Number Gussing Game! ")
    print("I'm thinking of a number between 1 and 100. ")
    turns = level_set()
    # print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make guess: "))
        turns = check_ans(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess == answer:
            print("Guess agin.")


game()


# print(f"{attempts} and {answer}")

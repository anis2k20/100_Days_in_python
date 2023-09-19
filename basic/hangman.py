import random

word_list = ["apple", "banana", "cherry"]
choose = random.choices(word_list)
userChoose = ""

length = len(str(choose)) - 4

for i in range(length):
    print("_", end=" ")


for i in range(length):
    ltr = input(("\nGuess a letter:"))
    userChoose += ltr
    comp(ltr, i)


print(f"{choose},{length},{userChoose}")

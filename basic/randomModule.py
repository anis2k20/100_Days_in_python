import random
name_str = input("Give me everybody name, seperated by a comma: ")

names = name_str.split(", ")

biller_name = random.choice(names)
print(f"{biller_name} going to buy the meal today!")
import random
import string

print("Welcome to the PyPassword Generator.")

latter = int(input("How many latter would in your password: "))
symbol = int(input("How many symbol would you like: "))
num = int(input("How many number would you like: "))

password = " "

total = latter + symbol + num

ranNumForUl = random.randint(1, latter)
ranNumForll = latter - ranNumForUl

ll = "".join(random.choices(string.ascii_lowercase, k=ranNumForUl))
ul = "".join(random.choices(string.ascii_uppercase, k=ranNumForll))

smbl = "".join((random.choices(string.punctuation, k=symbol)))

digit = "".join(random.choices(string.digits, k=num))

all_ele = str(ul + ll + smbl + digit)

print("".join(random.sample(all_ele, total)))

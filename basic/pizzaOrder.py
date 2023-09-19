print("Welcome to the python pizza delivery.")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

S=15
M=20
L=25

pForS=2
pForM=3
pForL=3

eCzP = 1

bill = 0
"""""
if size == "S":
    bill += S
if add_pepperoni == "Y":
    if size == "S":
        bill += pForS
    else:
        bill += pForM

if extra_cheese == "Y":
    bill += eCzP

print("Your final bill is: $",bill,".")
"""

if size == "S":
    bill += S
    if add_pepperoni == "Y":
        bill += pForS
        if extra_cheese == "Y":
            bill += eCzP
            print("Your final bill is: $",bill,".")
        elif extra_cheese == "N":
            print("Your final bill is: $",bill,".")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += eCzP
            print("Your final bill is: $",bill,".")
        elif extra_cheese == "N":
            print("Your final bill is: $",bill,".")
        
if size == "M":
    bill += M
    if add_pepperoni == "Y":
        bill += pForM
        if extra_cheese == "Y":
            bill += eCzP
            print("Your final bill is: $",bill,".")
        elif extra_cheese == "N":
            print("Your final bill is: $",bill,".")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += eCzP
            print("Your final bill is: $",bill,".")
        elif extra_cheese == "N":
            print("Your final bill is: $",bill,".")

if size == "L":
    bill += L
    if add_pepperoni == "Y":
        bill += pForL
        if extra_cheese == "Y":
            bill += eCzP
            print("Your final bill is: $",bill,".")
        elif extra_cheese == "N":
            print("Your final bill is: $",bill,".")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += eCzP
            print("Your final bill is: $",bill,".")
        elif extra_cheese == "N":
            print("Your final bill is: $",bill,".")
    
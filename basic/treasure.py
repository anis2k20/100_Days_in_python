
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choose1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()
if choose1 == "left":
    choose2 = input("You're at a cross road. Where do you want to go? Type 'swim' or 'wait': ").lower()
    if choose2 == "wait":
        choose3 = input("You're at a cross road. Where do you want to go? Type 'red' or 'blue' or yellow: ").lower()
        if choose3 == "yellow":
            print("You Win!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
        elif choose3 == "red":
            print("Burned by fire. Game Over.")
        elif choose3 == "blue":
            print("Eaten by beasts. Game Over.")
    
    elif choose2 == "swim":
        print("Attacked by trout. Game Over.")

elif choose1 == "right":
    print("Fall into a hole.\nGame Over.")
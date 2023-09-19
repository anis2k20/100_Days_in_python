print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $ "))

tip = int(input("What perchantage tip would you like to give? 10, 12, or 15? "))

numOfPeople = int(input("How many people split the bill? "))

totalBill = ((tip*bill)/100 + bill)

perPersonBill = round(totalBill/numOfPeople,2)

print("Each person should pay: $",perPersonBill)
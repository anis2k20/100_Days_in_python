name1 = input("Enter your name: ").lower()
name2 = input("Enter your partner name: ").lower()
twoName = name1+name2

t=r=u=e=l=o=v=e=0

for i in twoName:
   
    if i=="t":
        t=t+1
    elif i=="r":
        r+=1
    elif i=="u":
        u+=1
    elif i=="e":
        e+=1
    elif i=="l":
        l+=1
    elif i=="o":
        o+=1
    elif i=="v":
        v+=1
    elif i=="e":
        i+=1

tr=(t+r+u+e)
lv=(l+o+v+e)

first = str(tr)
second = str(lv)

final = first+second
final_convert = int(final)

if final_convert<10 or final_convert>90:
    print(f"Your score is {final_convert}, You go together like coke and mentos.")
elif final_convert>=40 and final_convert<=50:
    print(f"Your score is {final_convert}, you are alright together.")
else:
    print(f"Your score is {final_convert}")


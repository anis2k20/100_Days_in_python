score = input("Enter scores: ")
all_score = score.split(",")
mx = int(all_score[0])

for s in all_score:
    S = int(s)
    if S>mx:
        mx=S

print(mx)
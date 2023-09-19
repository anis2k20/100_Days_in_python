height = input("Enter the all student heitht saperated by comma: ")
all_height = height.split(",")
sum = i = 0
for h in all_height:
    sum = sum + int(h)
    i+=1

avg = (sum//i)
#print(sum)
#print(i)
print(avg)

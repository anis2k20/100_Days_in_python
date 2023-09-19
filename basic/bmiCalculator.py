height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = float(weight/(height*height))

if bmi<18.5:
    print("Underweight")
elif 18.5<bmi<25:
    print("Normal")
elif 25<bmi<30:
    print("Overweight")
elif bmi>30:
    print("Obese")
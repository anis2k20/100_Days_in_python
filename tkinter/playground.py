

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#      return sum
#
# print(add(2,3,5))
# def calculate(**kwargs):
#     # for (key,value) in kwargs.items():
#     print(kwargs["multiply"])
#
# calculate(add=5, multiply=3)


fruits = ["Apple","Pear","Orange"]
def make_pie(index):
        try:
                fruit = fruits[index]
        except IndexError:
                print("Fruit Pie")
        else:
                print(fruit + " Pie")

make_pie(2)
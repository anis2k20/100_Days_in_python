"""
def greet():
    print("Hello world")
    print("Hello air")
    print("Hello nature")

greet()

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Anis")
"""
import math

wall_h = int(input("Enter your wall height: "))
wall_w = int(input("Enter your wall widht: "))
coverage = 5


def calcualtion_cans(wall_h, wall_w):
    cans = math.ceil((wall_h * wall_w) / coverage)
    print(f"You'll need {cans} cans")


calcualtion_cans(wall_h, wall_w)

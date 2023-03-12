#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
    print("last digit of {} is {} and is ".format(number, digit),
            end= "")
if digit > 5:
    print("greater than 5")
elif(number == 0):
    print(f"{number} is zero")
else:
    print(f"{number} is less than 6 or not 0")

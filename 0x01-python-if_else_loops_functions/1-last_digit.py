#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
if number < 0:
    last_digit = -(last_digit)
str = f"Last digit of {number} is {last_digit} and is"
if last_digit > 5:
    print(f'{str:s} greater than 5')
elif last_digit == 0:
    print(f"{str:s} 0")
elif (last_digit < 6) and (last_digit != 0):
    print(f"{str:s} less than 6 and not 0")
else:
    print("TypeError")

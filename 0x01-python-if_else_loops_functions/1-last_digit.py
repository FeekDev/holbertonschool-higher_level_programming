#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# take last digit
last_digit = number % 10

# check greather than 5
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")

# check las_digit is 0
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")

# check las_digit is 0
if last_digit < 6 and not last_digit < 0 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
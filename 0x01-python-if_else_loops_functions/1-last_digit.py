#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if number < 0:
    number = -number
last_digit = number % 10
if last_digit > 5:
    str_to_add = "and is greater than 5"
elif last_digit == 0:
    str_to_add = "and is 0"
else:
    str_to_add = "and is less than 6 and not 0"
print(f"Last digit of {n} is {last_digit} {str_to_add}")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_last_p = number % 10
n_last_n = number % -10
if number > 5:
    print(f"Last digit of {number} is {n_last_p} and is greater than 5")
if number == 0:
    print(f"Last digit of {number} is {n_last_p} and is 0")
if number < 6:
    print(f"Last digit of {number} is {n_last_n} and is less than 6 and not 0")


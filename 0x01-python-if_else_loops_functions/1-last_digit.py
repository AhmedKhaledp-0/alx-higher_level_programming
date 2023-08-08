#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = int(abs(number) % 10)
sts = "Last digit of "
if (number < 0):
    last_d = last_d * -1
if (last_d > 5):
    print(f"{sts}{number} is {last_d} and is greater than 5")
elif (last_d == 0):
    print(f"{sts}{number} is {last_d} and is 0")
else:
    print(f"{sts}{number} is {last_d} and is less than 6 and not 0")

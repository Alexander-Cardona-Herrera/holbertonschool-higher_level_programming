#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {:d} is {:d} "
if number < 0:
    lastdigit= ((number * -1) % 10) * -1
else:
    lastdigit= number % 10

if lastdigit > 5:
    print(str.format(number, lastdigit) + "and is greater than 5")
elif lastdigit < 6 and lastdigit != 0:
    print(str.format(number, lastdigit) + "and is less than 6 and not 0")
else:
    print(str.format(number, lastdigit) + "and is 0") 

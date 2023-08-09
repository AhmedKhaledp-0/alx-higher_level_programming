#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        y = ord(i)
        if y in range(97, 123):
            y = y - 32
        print("{:c}".format(y), end="")
    print("")

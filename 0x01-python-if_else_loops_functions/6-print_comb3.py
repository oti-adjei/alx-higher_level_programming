#!/usr/bin/python3
# Author - George

for dig1 in range(0, 10):
    for dig2 in range(dig1 + 1, 10):
        if dig1 == 8 and dig2 == 9:
            print("{}{}".format(dig1, dig2))
        else:
            print("{}{}".format(dig1, dig2), end=", ")

#!/usr/bin/python3

for i in range(122, 0, -1):
    if i < 97:
        break
    if i % 2 != 0:
        i -= 32
    print("{}".format(chr(i)), end="")

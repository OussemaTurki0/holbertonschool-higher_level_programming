#!/usr/bin/python3
def uppercase(str):
    for c in str:
        diff = ord('a') - ord('A') if 'a' <= c <= 'z' else 0
        print("{:c}".format(ord(c) - diff), end="")
    print("")

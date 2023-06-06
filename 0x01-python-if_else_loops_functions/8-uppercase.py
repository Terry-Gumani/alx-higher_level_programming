#!/usr/bin/env python3

def uppercase(s):
    for c in s:
        uppercase_char = chr(ord(c) - 32) if ord(c) >= 97 and ord(c) <= 122 else c
        print(uppercase_char, end="")
    print()

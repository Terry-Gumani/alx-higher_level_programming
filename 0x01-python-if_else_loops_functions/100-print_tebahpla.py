#!/usr/bin/python3

def print_reverse_alphabet():
    for i in range(90, 64, -1):
        print(chr(i + 32 if i % 2 == 0 else i), end="")

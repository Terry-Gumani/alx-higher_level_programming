#!/usr/bin/python3
# 3-infinite_add.py

import sys

def add_arguments(args):
    total = 0
    for arg in args:
        total += int(arg)
    return total

if __name__ == "__main__":
    arguments = sys.argv[1:]
    result = add_arguments(arguments)
    print(result)

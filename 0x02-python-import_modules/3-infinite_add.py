#!/usr/bin/python3

import sys

def add_arguments(argv):
    total = 0
    for arg in argv:
        total += int(arg)
    return total

result = add_arguments(sys.argv[1:])
print(result)


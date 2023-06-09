#!/usr/bin/python3

import sys

def print_arguments(argv):
    num_arguments = len(argv)
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
        print(f"1: {argv[0]}")
    else:
        print(f"{num_arguments} arguments:")
        for i, arg in enumerate(argv):
            print(f"{i+1}: {arg}")

print_arguments(sys.argv[1:])


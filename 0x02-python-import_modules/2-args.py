#!/usr/bin/python3
# 2-args.py

import sys

def print_arguments(argv):
    num_args = len(argv)

    if num_args == 0:
        print("0 argument(s).")
        print(".")
    else:
        print(f"{num_args} argument(s):")
        for i in range(num_args):
            print(f"{i+1}: {argv[i]}")

print_arguments(sys.argv[1:])


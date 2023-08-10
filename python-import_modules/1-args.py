#!/usr/bin/env python3
import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1
    plural = 's' if num_arguments != 1 else ''
    print("{num_arguments} argument{plural}:".format(num_arguments=num_arguments, plural=plural))
    
    if num_arguments > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{i}: {arg}".format(i=i, arg=arg))

if __name__ == "__main__":
    print_arguments()
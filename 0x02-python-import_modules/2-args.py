#!/usr/bin/python
import sys

if __name__ == '__main__':
    if len(sys.argv[1:]) < 1:
        print("{} arguments.".format(len(sys.argv[1:])))
    elif len(sys.argv[1:]) == 1:
        print("{} argument:".format(len(sys.argv[1:])))
    else:
        print("{} arguments:".format(len(sys.argv[1:])))
    for i in range(1, len(sys.argv[1:]) + 1):
        print("{}: {}".format(i, sys.argv[i]))

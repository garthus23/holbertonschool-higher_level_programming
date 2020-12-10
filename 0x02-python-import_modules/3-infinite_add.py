#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    result = 0
    if len(argv) == 1:
        print("{}".format(result))
    else:
        for i in range(1, len(argv)):
            result = result + int(argv[i])
        print("{}".format(result))

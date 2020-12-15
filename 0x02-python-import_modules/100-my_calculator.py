#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from sys import exit
    from calculator_1 import sub, mul, add, div

    operator = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    for i in operator:
        if i == argv[2]:
            print("{:d} {:s} {:d} = {:d}".format(a, i, b, operator[i](a, b)))
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
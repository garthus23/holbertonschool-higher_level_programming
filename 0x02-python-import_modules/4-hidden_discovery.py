#!/usr/bin/env python3.4

if __name__ == "__main__":
    import hidden_4

    for i in dir(hidden_4):
        if not "__" in i:
            print("{:s}".format(i))


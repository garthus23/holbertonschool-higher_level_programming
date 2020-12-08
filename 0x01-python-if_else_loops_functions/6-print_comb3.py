#!/usr/bin/python3
for i in range(1, 89):
    if i < 10:
        print("{:02d}".format(i), end=", ")
    else:
        if str(i)[0] < str(i)[1]:
            print(i, end=", ")
print("89")

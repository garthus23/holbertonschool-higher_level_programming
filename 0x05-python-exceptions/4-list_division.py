#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    n = 0

    for i in range(0, list_length):
        try:
            new_list.append(my_list_1[n] / my_list_2[n])
        except IndexError:
            print("out of range")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        n += 1
    return (new_list)

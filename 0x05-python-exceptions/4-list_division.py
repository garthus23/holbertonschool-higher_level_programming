#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    number = 0
    n = 0

    for i in range(0, list_length):
        try:
            number = my_list_1[n] / my_list_2[n]
        except IndexError:
            print("out of range")
            number = 0
        except ZeroDivisionError:
            print("division by 0")
            number = 0
        except TypeError:
            print("wrong type")
            number = 0
        finally:
            new_list.append(number)
        n += 1
    return (new_list)

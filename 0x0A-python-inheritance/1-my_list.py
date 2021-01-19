#!/usr/bin/python3


"""
    class of lists
"""


class MyList(list):
    """ class of list """
    pass

    def print_sorted(self):
        """ sort the list """
        if self is not None:
            x = self.copy()
            x = sorted(x)
            print(x)

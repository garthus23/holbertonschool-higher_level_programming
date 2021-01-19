#!/usr/bin/python3


"""
    class of lists
"""


class MyList(list):
    """ class of list """
    pass

    def print_sorted(self):
        """ sort the list """
        x = self.copy()
        return (x.sort())

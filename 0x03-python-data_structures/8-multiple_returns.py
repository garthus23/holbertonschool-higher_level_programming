#!/usr/bin/python3


def multiple_returns(sentence):

    mylist = []
    mylist.append(len(sentence))
    if len(sentence) > 0:
        mylist.append(sentence[0])
    else:
        mylist.append(None)

    return (tuple(mylist))

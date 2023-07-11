#!/usr/bin/python3
"""definition of fucntion that return pascale triangle"""


def pascal_triangle(n):
    """ fucntion that return pascale triangle """
    mylist = []
    if n <= 0:
        return mylist
    if n >= 1:
        mylist.append([1])
    for i in range(1, n):
        mylist.append([1])
        for j in range(len(mylist[i - 1]) - 1):
            mylist[i].append(mylist[i - 1][j] + mylist[i - 1][j + 1])
        mylist[i].append(1)
    return mylist

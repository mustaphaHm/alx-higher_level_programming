#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenTa = len(tuple_a)
    lenTb = len(tuple_b)
    for i in range(0, lenTa - 1):
        if lenTa == 2 and lenTb == 2:
            for j in range(0, lenTb - 1):
                a = tuple_a[i] + tuple_b[j]
                b = tuple_a[i + 1] + tuple_b[j + 1]
                newT = (a, b)
        elif lenTa == 2 and lenTb == 1:
            newT = (tuple_a[i] + tuple_b[i], tuple_a[i + 1])
        else:
            newT = (tuple_a[i], tuple_a[i + 1])
    return newT

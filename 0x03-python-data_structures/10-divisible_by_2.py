#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for el in my_list:
        if el % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList

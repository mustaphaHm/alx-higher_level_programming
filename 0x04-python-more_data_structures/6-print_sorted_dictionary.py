#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictKeys = list(a_dictionary.keys())
    sortedKeys = sorted(dictKeys)
    for el in sortedKeys:
        print("{} : {}".format(el, a_dictionary[el]))

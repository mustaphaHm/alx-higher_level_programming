#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for el in my_string:
        if el != "c" and el != 'C':
            newStr += el
    return newStr

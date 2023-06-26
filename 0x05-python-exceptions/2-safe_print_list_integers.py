#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        countInt = 0
        index = 0
        while index < x:
            if isinstance(my_list[index], int):
                print("{}".format(my_list[index]), end='')
                countInt += 1
            index += 1
    except IndexError:
        print()
        return countInt
    print()
    return countInt

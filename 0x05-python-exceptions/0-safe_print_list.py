#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for el in my_list:
            print(el, end='')
            count += 1
            if count == x:
                break
    except IndexError:
        print("Index Error")
    finally:
        print()
        return count

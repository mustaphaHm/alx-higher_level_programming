#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lenRow = len(row)
        for i in range(lenRow):
            print("{:d}".format(row[i]), end='')
            if i < lenRow - 1:
                print("{:d}".format(' '), end='')
        print("{}".format("$"))

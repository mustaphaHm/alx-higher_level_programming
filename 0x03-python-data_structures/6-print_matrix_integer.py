def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lenRow = len(row)
        for i in range(lenRow):
            print("{}".format(row[i]), end='')
            if i < lenRow - 1:
                print("{}".format(' '), end='')
        print("{}".format("$"))

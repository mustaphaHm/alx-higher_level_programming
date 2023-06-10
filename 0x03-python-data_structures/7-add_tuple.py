def add_tuple(tuple_a=(), tuple_b=()):
    lenTa = len(tuple_a)
    lenTb = len(tuple_b)
    if lenTa < 2:
        if lenTa == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if lenTb < 2:
        if lenTb == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

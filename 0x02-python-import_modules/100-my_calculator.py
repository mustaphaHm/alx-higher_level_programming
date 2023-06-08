#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc, sys

    num_args = len(sys.argv) - 1
    operators = """+ - * /"""
    if num_args < 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, calc.add(a, b)))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, calc.sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, calc.mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, calc.div(a, b)))

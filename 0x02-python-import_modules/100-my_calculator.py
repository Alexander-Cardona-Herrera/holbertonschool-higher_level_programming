#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    sym = str(sys.argv[2])
    if len(sys.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sym != "+" and sym != "-" and sym != "*" and sym != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if str(sys.argv[2]) == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif str(sys.argv[2]) == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif str(sys.argv[2]) == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))

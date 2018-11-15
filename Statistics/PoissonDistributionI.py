from math import exp, factorial


def poisson(x, lamb):
    return pow(lamb, x)*exp(-lamb)/factorial(x)


def main():
    mean = float(input())
    x = float(input())

    print("{0:.3f}".format(poisson(x, mean)))


if __name__ == '__main__':
    main()
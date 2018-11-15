def expectation(lamb):
    """ Given a poisson distribution with
    mean 'lamb', gives the expected value
    of X^2
    """
    return lamb + lamb**2


def main():
    mean1, mean2 = map(float, input().split())
    c1 = 160 + 40*expectation(mean1)
    c2 = 128 + 40*expectation(mean2)
    print("{0:.3f}".format(c1))
    print("{0:.3f}".format(c2))


if __name__ == '__main__':
    main()
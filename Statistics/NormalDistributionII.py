from math import erf, sqrt


def cumulative_normal(x, mi, sigma):
    """ Calculates the cumulative probability of
    a random event with normal distribution to happen
    with value x or less

    :param x: Value for the cumulative probability
    :param mi: Mean of the event
    :param sigma: Standard deviation of the event
    :return: P(X <= x)
    """
    return 0.5*(1 + erf((x-mi)/(sigma*sqrt(2))))


def main():
    mi, sigma = map(float, input().split())
    x1 = float(input())
    x2 = float(input())

    print("{0:.2f}".format(100*(1 - cumulative_normal(x1, mi, sigma))))
    print("{0:.2f}".format(100*(1 - cumulative_normal(x2, mi, sigma))))
    print("{0:.2f}".format(100*cumulative_normal(x2, mi, sigma)))


if __name__ == '__main__':
    main()

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
    max_weight = int(input())
    n_boxes = int(input())
    mean = float(input())
    std = float(input())

    mean = n_boxes*mean
    std = sqrt(n_boxes)*std

    print("{0:.4f}".format(cumulative_normal(max_weight, mean, std)))


if __name__ == '__main__':
    main()

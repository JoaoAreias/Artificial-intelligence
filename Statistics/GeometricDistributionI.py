def geometric(n, p):
    """Returns the probability of an event
    with probability 'p' of happening occurs
    after 'n' trials
    """
    return p*pow(1-p, n-1)


def main():
    # Event with probability p = r/q
    r, q = list(map(float, input().split()))
    # Number of trials
    n = int(input())

    p = r/q
    print("{0:.3f}".format(geometric(n, p)))


if __name__ == '__main__':
    main()

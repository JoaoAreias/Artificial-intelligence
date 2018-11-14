from math import factorial


def nCr(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))


def binomial(x, n, p):
    """Binomial distribution. Returns the probability of
    'x' successes in 'n' trials with probability of
    success 'p'"""
    return nCr(n, x)*pow(p, x)*pow(1-p, n-x)


def main():
    percentage, size = list(map(float, input().split()))
    # Probability of a piston being rejected
    p_rejected = percentage/100
    # Probability of no more than or equal to 2 being rejected
    p_less_than_2 = 0
    for i in range(3):
        p_less_than_2 += binomial(i, size, p_rejected)

    print("{0:.3f}".format(p_less_than_2))
    # P of at least 2 is just the complementary + P(2)
    print("{0:.3f}".format(1-p_less_than_2 + binomial(2, size, p_rejected)))


if __name__ == '__main__':
    main()

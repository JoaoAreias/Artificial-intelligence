from math import factorial


def nCr(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))


def main():
    # Ratio of boys to girls
    ratio1, ratio2 = list(map(float, input().split()))
    # Probability of a baby being a boy
    p_boy = ratio1/(ratio1+ratio2)
    # Probability of 3 or more babies being boys
    total_probability = 0
    for i in range(3, 7):
        total_probability += nCr(6, i)*pow(p_boy, i)*pow(1-p_boy, 6-i)

    print("{0:.3f}".format(total_probability))


if __name__ == '__main__':
    main()

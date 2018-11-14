def main():
    # Event with probability p = r/q
    r, q = list(map(float, input().split()))
    # Number of trials
    n = int(input())

    # Uses complementary probability
    probability = 1 - pow(1-(r/q), n)
    print("{0:.3f}".format(probability))


if __name__ == '__main__':
    main()

from math import sqrt


def main():
    size = int(input())
    mean = float(input())
    std = float(input())
    input()  # Probability
    z = float(input())

    print("{0:.2f}".format(mean - std*z/sqrt(size)))
    print("{0:.2f}".format(mean + std*z/sqrt(size)))


if __name__ == '__main__':
    main()

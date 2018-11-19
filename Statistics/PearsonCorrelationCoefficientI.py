from math import sqrt


def pearson_correlation(x, y):
    assert len(x) == len(y)
    # Mean and standard deviation
    mean_x = sum(x)/len(x)
    mean_y = sum(y)/len(y)
    std_x = sqrt(sum(map(lambda _x: (_x-mean_x)**2 / len(x), x)))
    std_y = sqrt(sum(map(lambda _y: (_y - mean_y) ** 2 / len(y), y)))
    # Computing covariance
    cov = sum(
        map(
            lambda _x, _y: (_x-mean_x)*(_y-mean_y),
            x, y
        )
    )/len(x)
    return cov/(std_x*std_y)


def main():
    input()
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    print("{0:.3f}".format(pearson_correlation(x, y)))


if __name__ == '__main__':
    main()

def main():
    x, y = [], []
    for _ in range(5):
        _x, _y = map(float, input().split())
        x.append(_x)
        y.append(_y)

    size = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    mean_x = sum_x/size
    mean_y = sum_y/size

    b = (
            (size*sum(map(lambda _x, _y: _x*_y, x, y)) - sum_x*sum_y) /
            (size*sum(map(lambda _x: _x**2, x)) - sum_x**2)
    )
    a = mean_y - b*mean_x

    print("{0:.3f}".format(a + b*80))


if __name__ == '__main__':
    main()

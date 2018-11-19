def get_rank(X):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(X)))
    return [x_rank[x] for x in X]


def main():
    size = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    rx = get_rank(x)
    ry = get_rank(y)

    d = [(rx[i] - ry[i])**2 for i in range(size)]
    rxy = 1 - 6*sum(d)/(size*(size**2 - 1))
    print("{0:.3f}".format(rxy))


if __name__ == '__main__':
    main()

from numpy.linalg import inv
import numpy as np


def main():
    # Get data input
    m, n = map(int, input().split())
    A, y = [], []

    for line in range(n):
        data = list(map(float, input().split()))
        A.append([1] + data[:-1])
        y.append(data[-1])

    A = np.array(A)
    y = np.array(y)

    # Fit the linear regression
    pseudo_inv = np.matmul(inv(np.matmul(A.T, A)), A.T)
    regression = np.matmul(pseudo_inv, y)

    # Retrieve Andrea's querry
    q = int(input())
    for querry in range(q):
        # Get input
        x = np.hstack((
            [1],
            list(map(float, input().split()))
        ))
        # Predict output
        print(np.matmul(regression, x))

if __name__ == '__main__':
    main()

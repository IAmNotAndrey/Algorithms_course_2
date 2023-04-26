from math import inf
from pprint import pprint


def get_path(a_matrix, p_matrix, start, end):
    path = [start + 1]
    path_len = 0
    while start != end:
        save_start = start
        start = p_matrix[start][end] - 1
        path_len += a_matrix[save_start][start]
        path.append(start + 1)

    return path, path_len


if __name__ == '__main__':
    # Матрица длин дуг ориентированного n-вершинного графа

    # A = [
    #     [0, 2, inf, 3, 1, inf, inf, 10],
    #     [2, 0, 4, inf, inf, inf, inf, inf],
    #     [inf, 4, 0, inf, inf, inf, inf, 3],
    #     [3, inf, inf, 0, inf, inf, inf, 8],
    #     [1, inf, inf, inf, 0, 2, inf, inf],
    #     [inf, inf, inf, inf, 2, 0, 3, inf],
    #     [inf, inf, inf, inf, inf, 3, 0, 1],
    #     [10, inf, 3, 8, inf, inf, 1, 0],
    # ]

    # A = [
    #     [0, 8, 5],
    #     [3, 0, inf],
    #     [inf, 2, 0]
    # ]

    # A = [
    #     [0, 2, 1, -2],
    #     [inf, 0, -1, -1],
    #     [1, inf, 0, inf],
    #     [inf, 3, 2, 0]
    # ]

    # # S A B C 1 2
    # A = [
    #     [0, 0, 0, 0, inf, inf],
    #     [0, 0, inf, inf, -15, -10],
    #     [0, inf, 0, inf, -10, -15],
    #     [inf, inf, 0, 0, -8, -20],
    #     [inf, 15, 10, 8, 0, inf],
    #     [inf, 10, 15, 20, inf, 0],
    # ]

    # # S A B C 1 2
    # A = [
    #     [0, 0, 0, 0, inf, inf],
    #     [0, 0, inf, inf, -300, 0],
    #     [0, inf, 0, inf, -10, -75],
    #     [inf, inf, 0, 0, 0, -100],
    #     [inf, 0, 150, 80, 0, inf],
    #     [inf, 200, 150, 100, inf, 0],
    # ]

    # S A B C 1 2
    A = [
        [0, 0, 0, 0, inf, inf],
        [0, 0, inf, inf, 0, -100],
        [0, inf, 0, inf, -100, 0],
        [inf, inf, 0, 0, -80, 0],
        [inf, 0, 300, 50, 0, inf],
        [inf, 0, 225, 200, inf, 0],
    ]

    n = len(A)
    P = [[i for i in range(1, n + 1)] for j in range(1, n + 1)]

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    P[i][j] = k + 1

    pprint(A, width=50)
    print()
    pprint(P, width=50)
    print()

    # start = 2
    # end = 4
    #
    # path, path_len = get_path(A, P, start - 1, end - 1)
    #
    # print(path)
    # print(path_len)

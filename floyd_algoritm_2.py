from math import inf
from pprint import pprint
from copy import deepcopy


def get_inital_t_matrix(n: int) -> list:
    row = []
    for i in range(1, n + 1):
        row.append(i)
    matrix = [[elem for elem in row] for _ in range(n)]
    return matrix


def get_zero_matrix(n: int) -> list:
    row = []
    for i in range(0, n):
        row.append(0)
    matrix = [[elem for elem in row] for _ in range(n)]
    return matrix


def get_new_d_t_matrixes(prev_d: list, prev_t: list, k: int = 0) -> tuple[list]:
    n = len(prev_d)

    # region Проверка на корректность введённых данных
    if not isinstance(prev_d, list):
        raise ValueError(prev_d)
    if not isinstance(prev_t, list):
        raise ValueError(prev_t)
    if not isinstance(k, int):
        raise ValueError(k)

    # Проверка на то, является ли матрица `prev_d` равносторонней
    if not all(len(row) == n for row in prev_d):
        raise ValueError(prev_d)
    # Проверка на то, являются ли длина матрицы `prev_t` == n
    if len(prev_t) != n:
        raise ValueError(prev_t)
    # Проверка на то, является ли матрица `prev_t` равносторонней
    if not all(len(row) == n for row in prev_t):
        raise ValueError(prev_t)
    # endregion

    # Если `k` == размеру матрицы, то заканчиваем работу алгоритма
    if k == len(prev_d):
        return prev_d, prev_t

    # Создаём макет матрицы `new_d`
    new_d = [[None] * n for _ in range(n)]
    # Делаем копию макета для `new_t`
    new_t = deepcopy(new_d)

    for i in range(n):
        for j in range(n):
            # NOTE: ставим k-1
            # Расчёты для i,j-элемента матрицы `new_d`
            new_d[i][j] = min(
                [prev_d[i][j], prev_d[i][k - 1] + prev_d[k - 1][j]]
            )
            # Расчёты для i,j-элемента матрицы `new_t`
            if new_d[i][j] == prev_d[i][j]:
                new_t[i][j] = prev_t[i][j]
            else:
                new_t[i][j] = prev_t[i][k - 1]

    return get_new_d_t_matrixes(new_d, new_t, k + 1)


def find_shortest_way_by_floyd(
        a: int,
        b: int,
        t: list) -> list:
    '''Находит кратчайшее расстояние из точки `a` в точку `b`. Выводит путь в виде списка индексов. Отсчёт нумерации точек ведётся с 0 до n-1.'''

    # NOTE: использование `a` и `b` в коде ведётся только с операцией декримента

    if a == b:
        return [a]
    elif a > b:
        a, b = b, a

    way = [a]
    cur_pos = a
    while cur_pos != b:
        next_pos = t[cur_pos][b]
        way.append(next_pos)
        cur_pos = next_pos

    return way


if __name__ == '__main__':
    # Матрица длин дуг ориентированного n-вершинного графа
    A = [
        [0, 2, 1, -2],
        [inf, 0, -1, -1],
        [1, inf, 0, inf],
        [inf, 3, 2, 0]
    ]
    # Матрица T
    n = 4
    P = get_zero_matrix(n)

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    P[i][j] = k + 1

    pprint(A, width=40)
    print()
    pprint(P, width=40)
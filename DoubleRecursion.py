import time
import pprint

# Задаём кол-во элементов
n = 6

# Задаём кол-во позиций
k = 2

# Считаем кол-во выполнений для функций
count = [0]


def paskal(n, k):
    """Расчёт кол-ва сочетаний через треугольник Паскаля"""
    count[0] += 1

    if k == 0:
        return 1

    if n == k:
        return 1

    return paskal(n - 1, k - 1) + paskal(n - 1, k)


def recur_relation(n, k):
    """Расчёт кол-ва сочетаний через рекурентные соотношения"""
    count[0] += 1

    if k == 0:
        return 1

    return n / k * recur_relation(n - 1, k - 1)


print('Введите:\n1 - чтобы вычислить кол-во для введённых N и K;\n2 - чтобы провести сравнение времени.')
choose = input()
print()

if choose == '1':
    # Через треугольник Паскаля
    current_time = time.perf_counter()
    print('Метод Паскаля:')
    print('Результат:', paskal(n, k))
    time_paskal = time.perf_counter() - current_time
    print('Время:', time_paskal)
    print('Кол-во выполнений:', count[0] - 2)
    print()
    count[0] = 0

    # Через рекурентные соотношения
    current_time = time.perf_counter()
    print('Метод рекур. соотношений:')
    print('Результат:', recur_relation(n, k))
    time_recur = time.perf_counter() - current_time
    print('Время:', time_recur)
    print('Кол-во выполнений:', count[0] - 1)
    print()

    # Сравнение
    print('Рекур/Паскаль:', round(time_recur/time_paskal, 2))

elif choose == '2':
    # Комплексное сравнение для n=1..10 и k=1..n (k < n)
    matrix = []

    # n = i
    for i in range(2, 10):
        matrix.append([])

        # k = j
        for j in range(1, i):
            current_time = time.perf_counter()
            paskal(i, j)
            time_paskal = time.perf_counter() - current_time

            current_time = time.perf_counter()
            recur_relation(i, j)
            time_recur = time.perf_counter() - current_time

            matrix[i - 2].append(float(f'{time_recur/time_paskal:.2f}'))

    print('n - по вертикали, k - по горизонтали:')
    pprint.pprint(matrix)

    print('\nМин:', min(map(min, matrix)))
    print('Макс:', max(map(max, matrix)))
    print('Сред:', f'{sum(map(sum, matrix)) / sum(map(len, matrix)):.2f}')

else:
    print('Введите 1 или 2!')

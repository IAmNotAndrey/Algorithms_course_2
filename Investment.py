# Для удобного вывода
from pprint import pprint
import random

# # Размеры инвестиций
# investments = [100, 200, 300, 400, 500]
#
# # Матрица прибыли от проектов: строки = проекты
# start_project_matrix = [
#     [15, 20, 26, 34, 40],
#     [18, 22, 28, 33, 39],
#     [16, 23, 27, 29, 41],
#     [17, 19, 25, 31, 37]
# ]

# Размеры инвестиций
investments = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]

# Матрица прибыли от проектов: строки = проекты
# start_project_matrix = [
#     [15, 20, 26, 34, 40, 45, 51, 56, 61, 67, 73, 77],
#     [18, 22, 28, 33, 39, 43, 52, 54, 62, 65, 74, 78],
#     [16, 23, 27, 29, 41, 44, 50, 53, 64, 67, 75, 79],
#     [17, 19, 25, 31, 37, 45, 49, 55, 62, 68, 74, 80]
# ]

# Рандомайзер для заполнения матрицы прибыли от проектов
start_project_matrix = []
def random_profit():
    for i in range(4):
        current = 10
        project = []
        for j in range(len(investments)):
            current += random.randint(1, 11)
            project.append(current)
        start_project_matrix.append(project)
        project = []
random_profit()


# Количество вариантов инвестиций
invest_count = len(investments)

# Количество проектов
project_count = len(start_project_matrix)


def proportion_invest(project_matrix):
    """Расчёт наибольшей прибыли для пропорциональных и равномерных размеров инвестиций"""

    # Пока не дойдём до последних 2 проектов
    while len(project_matrix) > 1:
        # Комбинации
        combinations = []

        # Максимальные прибыли
        max_numbers = []

        # Проекты, с которыми ведётся работа на текущей итерации
        A = project_matrix[0]
        B = project_matrix[1]

        # Создаём массив: [прибыль, необходимая для неё инвестиция]
        # Прибыль и инвестиции берём из сочетаний проектов из A и B
        # Перебираем все сочетания
        for i in range(invest_count - 1):
            for j in range(invest_count - 1 - i):
                combinations.append((sum([investments[i], investments[j]]), sum([A[i], B[j]])))

        # Сортируем сочетания по необходимым инвестициям
        combinations.sort(key=lambda x: x[0])

        # Перебираем поочерёдно все инвестиции
        for i in range(invest_count):
            max_number = 0

            money = investments[i]

            # Проверяем крайние варианты: всё отдать в A или в B
            if A[i] >= B[i]:
                max_number = A[i]
            else:
                max_number = B[i]

            # Для каждого размера инвестиций находим максимум
            j = 0

            comb_count = len(combinations)

            while j < comb_count and combinations[j][0] <= money:
                current_number = combinations[j][1]

                if current_number > max_number:
                    max_number = current_number

                j += 1

            # Удаляем уже проверенные инвестиции
            combinations = combinations[j:]

            # Добавляем в список найденную для текущей инвестиции макс. прибыль
            max_numbers.append(max_number)

        # Удаляем проект A и вставляем на место B проект AB
        del project_matrix[0]
        project_matrix[0] = max_numbers

    return max_numbers


def create_empty_array(length):
    """Создание массива из пустых массивов"""

    arr = []

    for i in range(length):
        arr.append([])

    return arr


def create_zero_array(length):
    """Создание массива из нулей"""

    arr = []

    for i in range(length):
        arr.append(0)

    return arr


def check_all_combinations(project_matrix, investing_count, project_counts):
    """Расчёт наибольшей прибыли для пропорциональных и равномерных размеров инвестиций методом полного перебора"""

    # Создаём массив для максимальных прибылей
    max_project_sums = create_zero_array(investing_count)

    # Перебираем кол-во инвестиций
    for current_invest_count in list(range(1, investing_count + 1)):

        # Создаём массив для текущей комбинации
        current_comb = create_zero_array(current_invest_count)

        # Позиция указателя: прошлая и текущая
        last_pos = 0
        pos_find = -1

        # Сюда будем добавлять массивы с указанным размером инвестиции в каждый проект
        combs_investing = []

        # Генерируем сочетания с повторениями: N = кол-во проектов, K = кол-во инвестиций
        while True:
            # Считаем кол-во каждого проекта и записываем в матрицу сочетаний инвестиций
            combs_investing.append(create_zero_array(project_counts))

            for elem in current_comb:
                combs_investing[-1][elem] += 1

            # Сохраняем позицию указателя
            last_pos = pos_find

            # Сбрасываем позицию
            pos_find = -1

            # Ищем элемент, такой что: elem < N - 1
            for pos in range(current_invest_count):
                if current_comb[pos] < project_counts - 1:
                    pos_find = pos
                    break

            # Если элемент не найден, выходим из цикла
            if pos_find < 0:
                break

            # Если указатель не сдвинулся, увеличиваем текущий элемент
            if pos_find == last_pos:
                current_comb[pos_find] += 1

            else:
                # Увеличиваем уже следующий элемент
                current_comb[pos_find] += 1

                # Приравниваем все предыдущие к нему
                for pos in range(pos_find):
                    current_comb[pos] = current_comb[pos_find]

                # Сбрасываем указатель
                pos_find = 0

        # Максимальная прибыль
        max_project_sum = 0
        current_sum = 0

        # Перебираем матрицу инвестиций вида: [размер для 1-го проекта; размер для 2-го проекта; ...]
        for invests in combs_investing:
            for proj_num in range(project_counts):
                # В матрице project_matrix получаем элемент по номеру проекта и размеру инвестиции
                if invests[proj_num] > 0:
                    current_sum += project_matrix[proj_num][invests[proj_num] - 1]

            # Ищем максимальную прибыль
            if current_sum > max_project_sum:
                max_project_sum = current_sum

            current_sum = 0

        # Записываем прибыль в список
        max_project_sums[current_invest_count-1] = max_project_sum

    return max_project_sums


# Ищем прибыль сперва эффективным алгоритмом, затем полным перебором
print(proportion_invest(start_project_matrix.copy()))
print(check_all_combinations(start_project_matrix.copy(), invest_count, project_count))

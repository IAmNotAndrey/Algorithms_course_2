from pprint import pprint
import json
import copy

# Граф - уровневая стратегия
# pred_task_table_lev = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
# next_task_table_lev = ['B', 'C', 'L', 'D', 'A', 'A', 'A', 'L', 'E', 'E', 'C', 'B']
# worker_count_lev = 3

# Граф - уровневая и лексикографическая стратегии
# pred_task_table_lex = ['A', 'A', 'C', 'C', 'D', 'E', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'L']
# next_task_table_lex = ['B', 'J', 'E', 'F', 'E', 'H', 'H', 'J', 'K', 'A', 'G', 'H', 'L', 'G']
# worker_count_lex = 2

# Задачи из презентации
# Уровневая стратегия
# pred_task_table_lev = ['L', 'H', 'E', 'A', 'F', 'N', 'C', 'D', 'K', 'G', 'J', 'I', 'M']
# next_task_table_lev = ['N', 'B', 'H', 'N', 'L', 'B', 'L', 'A', 'G', 'A', 'B', 'G', 'L']
# worker_count_lev = 3

# Лексикографическая стратегия
pred_task_table_lex = ['D', 'K', 'G', 'G', 'A', 'K', 'D', 'J', 'F', 'D', 'J', 'J', 'F', 'B', 'F', 'D']
next_task_table_lex = ['C', 'C', 'H', 'E', 'E', 'E', 'G', 'G', 'G', 'A', 'A', 'K', 'K', 'K', 'E', 'H']
worker_count_lex = 2

# # Лексикографическая стратегия (прошлая)
# pred_task_table_lex = ['D', 'K', 'G', 'G', 'A', 'K', 'D', 'J', 'F', 'D', 'J', 'J', 'F', 'B']
# next_task_table_lex = ['C', 'C', 'H', 'E', 'E', 'E', 'G', 'G', 'G', 'A', 'A', 'K', 'K', 'K']
# worker_count_lex = 2

# =======================================================================================
# ================================ Доп функционал =======================================
# =======================================================================================


def build_graph(relations: dict, roots: list, graph_link: dict = {}) -> dict:
    """Построение графа-дерева"""

    # Перебираем текущие корни
    for point in roots:
        # Для конечных вершин
        check_end = False
        end_chars = []

        # Перебираем связанные вершины
        for next_point in relations[point]:
            # Если вершина не имеет потомков
            if next_point not in relations.keys():
                end_chars.append(next_point)

        # Делаем копию, чтобы не портить список связей
        relations_copy = copy.deepcopy(relations)

        # Удаляем конечные вершины, они не имею потомков
        for remove_char in end_chars:
            relations_copy[point].remove(remove_char)

        # print(point, ':', end_chars, '||', relations_copy[point])

        # Если были удалены все вершины
        if len(relations_copy[point]) == 0:
            graph_link[point] = end_chars
            continue

        # Если нашлась хоть одна конечная вершина
        if len(end_chars) != 0:
            check_end = True

        # Если список с вершинами ещё не создан
        if point not in graph_link.keys():
            if check_end:
                # Добавляем в список конечные вершины и новый корень дерева, который передаём дальше
                graph_link[point] = [*end_chars, {}]
                build_graph(relations, relations_copy[point], graph_link[point][-1])
            else:
                # Передаём новый корень дерева дальше
                graph_link[point] = {}
                build_graph(relations, relations_copy[point], graph_link[point])

        else:
            if check_end:
                # Добавляем в список конечные вершины и НЕ ПУСТОЙ корень дерева
                graph_link[point] = [*end_chars, graph_link[point]]
            else:
                # Добавляем в список новый корень
                graph_link[point] = [graph_link[point], {}]

            build_graph(relations, relations_copy[point], graph_link[point][-1])

    return graph_link


def build_reverse_graph(relations: dict, graph_link: dict = {}) -> dict:
    """Построение перевёрнутого графа-дерева"""

    reversed_relations = {}

    # Переворачиваем дерево связей
    for item in relations.items():
        for value in item[1]:
            # Если значение есть - добавляем
            if value in reversed_relations.keys():
                reversed_relations[value].append(item[0])
            # Если нет - создаём новый список
            else:
                reversed_relations[value] = [item[0]]

    new_roots = []
    relation_keys = relations.keys()

    # Ищем новые корни
    for item in relations.items():
        for value in item[1]:
            if value not in relation_keys:
                new_roots.append(value)

    # pprint(reversed_relations)
    # print(new_roots)

    # Строим граф по перевёрнутым связям и новым корням
    return build_graph(reversed_relations, new_roots, {})


def create_print_graphs(pred_task_table: list, next_task_table: list):
    """Строит и выводит в консоль обычный и перевёрнутый графы"""

    # Длинна таблицы
    table_length = len(next_task_table)

    # Связи между предками и потомками
    relations = {}

    # Корни дерева
    roots = []

    # Создаём словарь связей между pred и next
    for i in range(table_length):
        next = next_task_table[i]
        pred = pred_task_table[i]

        # Для каждого предка указываем потомков
        if next not in relations.keys():
            # Если список ещё не создан, создаём его
            relations[next] = []

        relations[next].append(pred)

        # Ищем корни (вершины, не имеющие предков)
        if next not in pred_task_table:
            if next not in roots:
                roots.append(next)

    print('Relations:')
    pprint(relations)

    print('\nRoots:', roots, '\n')

    # Построение и печать графов
    graph = build_graph(copy.deepcopy(relations), copy.deepcopy(roots))
    print('===========================================\nGraph:')
    print(json.dumps(graph, indent=4))

    print('\n===========================================\nReversed graph:')

    reversed_graph = build_reverse_graph(relations, {})
    print(json.dumps(reversed_graph, indent=4))


# =======================================================================================
# ============================== Основной функционал ====================================
# =======================================================================================


def find_transit_ways_rec(relations: dict, points: list, transit_ways: list, ways_list: list = []) -> list:

    for point in points:
        if point in relations.keys():
            # Перебираем связанные вершины
            for next_point in relations[point]:
                if next_point in transit_ways:
                    ways_list.append(next_point)

                # Если вершина имеет потомков
                if next_point in relations.keys():
                    find_transit_ways_rec(relations, relations[point], transit_ways, ways_list)

    return ways_list


def find_transit_ways(pred_task_table: list, next_task_table: list) -> dict:
    # Длинна таблицы
    table_length = len(next_task_table)

    # Связи между предками и потомками
    relations = {}

    # Корни дерева
    roots = []

    # Создаём словарь связей между pred и next
    for i in range(table_length):
        next = next_task_table[i]
        pred = pred_task_table[i]

        # Для каждого предка указываем потомков
        if next not in relations.keys():
            # Если список ещё не создан, создаём его
            relations[next] = []

        relations[next].append(pred)

        # Ищем корни (вершины, не имеющие предков)
        if next not in pred_task_table:
            if next not in roots:
                roots.append(next)

    ways_list = {}

    for point in relations.keys():
        ways_list[point] = find_transit_ways_rec(relations, relations[point], relations[point], [])

    return ways_list


def remove_duplicate(first_list_link: list, second_list: list):
    """Удаляет из первого списка те элементы, которые есть во втором"""

    i = 0
    while i < len(first_list_link):
        if first_list_link[i] in second_list:
            del first_list_link[i]
        else:
            i += 1


def fill_task_on_graph(relations: dict, roots: list) -> list:
    """Создаёт список вершин (работ) по уровневой стратегии начиная с корней"""

    # Добавляем корни в начало списка
    task_list = [*roots]

    while True:
        new_roots = []

        for root in roots:
            if root in relations.keys():
                # Получаем список связей текущей вершины
                temp_new_roots = [*relations.get(root)]

                # Удаляем те вершины, которые уже есть в списке новых вершин (иначе в основу может добавиться AA, BB...
                # вместо одной A, B)
                remove_duplicate(temp_new_roots, new_roots)

                # Добавляем полученные точки в список новых вершин
                new_roots = [*new_roots, *temp_new_roots]

        if len(new_roots) == 0:
            break

        # Удаляем те вершины, которые уже есть в списке (иначе к A в основе может добавиться ещё одна A)
        remove_duplicate(new_roots, task_list)

        # Добавляем вершины в основной список
        task_list = [*task_list, *new_roots]

        # Обновляем список корней
        roots = new_roots

    return task_list


def fill_task_on_graph_lex(relations: dict, rev_relations: dict, roots: list) -> list:
    """Создаёт список вершин (работ) по уровневой и лексикографической стратегиям начиная с корней"""

    # Список вершин
    task_list = []

    # Список номеров вершин
    task_lex_words = {}

    # Присваиваем начальные номера корням
    i = 1
    for root in roots:
        task_lex_words[root] = str(i)
        i += 1

    while True:
        # Новые корни
        new_roots = []

        # Список для сравнения вершин по лексикографической стратегии
        temp_lex_words = []

        root_number = 0

        while root_number < len(roots):
            root = roots[root_number]
            root_order_error = False

            # Если у корня есть потомки
            if root in relations.keys():
                # Получаем список потомков
                temp_new_roots = [*relations.get(root)]

                # Удаляем те вершины, которые уже есть в списке новых вершин (иначе в основу может добавиться AA, BB...
                # вместо одной A, B)
                remove_duplicate(temp_new_roots, new_roots)
                remove_duplicate(temp_new_roots, [*task_lex_words.keys()])

                # Для каждой вершины записываем строку, состоящую из номеров её предков
                for new_root in temp_new_roots:
                    lex_str = ''

                    for relate_point in rev_relations[new_root]:
                        if relate_point not in task_lex_words.keys():
                            new_roots.append(roots[root_number])
                            # print(relate_point, roots[root_number])
                            del roots[root_number]
                            root_order_error = True
                            break
                        else:
                            # Тут мы должны добавлять номера в порядке убывания, то есть 654...
                            if len(lex_str) != 0:
                                if task_lex_words[relate_point] <= lex_str[-1]:
                                    lex_str += task_lex_words[relate_point]

                                else:
                                    for j in range(len(lex_str)):
                                        if task_lex_words[relate_point] > lex_str[j]:
                                            lex_str = lex_str[:j] + task_lex_words[relate_point] + lex_str[j:]
                                            break

                            else:
                                lex_str += task_lex_words[relate_point]

                    if root_order_error:
                        break

                    temp_lex_words.append([new_root, lex_str])

                if not root_order_error:
                    # Добавляем полученные точки в список новых вершин
                    new_roots = [*new_roots, *temp_new_roots]

            if not root_order_error:
                root_number += 1

        # Если ни у одного корня нет потомков (все конечные)
        if len(new_roots) == 0:
            break

        # Сортируем вершины согласно лексикографической стратегии
        temp_lex_words.sort(key=lambda x: x[1])

        # Добавляем номера вершин в основной список
        for pair in temp_lex_words:
            task_lex_words[pair[0]] = str(i)
            print(pair[0], pair[1])
            i += 1

        # Обновляем корни
        roots = new_roots

    print('\nWorks priority:')
    pprint(task_lex_words)

    # Переписываем вершины в список (гм... словарь автоматически выдаёт сортированный список, ну ок)
    for item in task_lex_words.items():
        task_list.append(item[0])

    return task_list


def create_gantt_diagram(relations: dict, works: list, worker_count: int) -> list:
    # ====================================================================
    # Диаграмма Ганта
    gant_diagram = [[]]

    # Уже завершённые задачи (для проверки возможности выполнения в текущей итерации)
    finished_tasks = []

    # Номер итерации (или время)
    iter_num = 0

    i = 0

    # Общее рабочее время
    work_time = len(works)

    # Заполняем диаграмму Ганта
    # Рабочее время может расти, в связи с появлением пробелов в диаграмме
    while i < work_time:
        # При переходе на следующую итерацию (следующий момент времени)
        if i % worker_count == 0 and i > 0:
            # Добавляем в список выполненные на текущей итерации задачи
            finished_tasks = [*finished_tasks, *gant_diagram[iter_num]]
            iter_num += 1
            gant_diagram.append([])

        # Номер задачи, которая будет выполняться, если текущую нельзя будет начать (пред задачи не будут завершены)
        next_task_number = i + 1

        while True:
            # Если у задачи нет предков, сразу добавляем её в список
            if works[i] not in relations.keys():
                break

            # Можно ли выполнять текущую задачу
            rigth_task = True

            # Список предков для текущей задачи
            for pred_task in relations.get(works[i]):

                # Если предыдущая задача не выполнена
                if pred_task not in finished_tasks:

                    # Если мы находимся не на конце
                    if next_task_number < len(works):
                        # Говорим, что задача не может быть выполнена и меняем её местами с next_task_number
                        rigth_task = False
                        works[i], works[next_task_number] = works[next_task_number], works[i]

                        # Если и следующую пока нельзя будет выполнить, пойдём дальше, пока не выйдем за границы
                        next_task_number += 1

                    else:
                        # Мы дошли до конца, нед задач, готовых к выполнению на текущий итерации
                        # Убираем нашу задачу обратно в конец
                        works.append(works[i])

                        # Ставим пробел и увеличиваем рабочее время
                        works[i] = '-'
                        work_time += 1

                    break

            # Пока задача не может быть выполнена, продолжаем поиск
            if not rigth_task:
                continue

            # Если она может быть выполнена - выходим из цикла
            break

        # Добавляем задачу в диаграмму Ганта
        gant_diagram[iter_num].append(works[i])

        i += 1

    # ====================================================================
    # Переворачиваем диаграмму, чтобы она отображалась как надо
    rotate_diagram = []

    for work in range(worker_count):
        rotate_diagram.append([])

    current_work_count = 0

    for iter_number in range(len(gant_diagram)):
        for worker in range(worker_count):
            if current_work_count == work_time:
                break

            current_work_count += 1
            rotate_diagram[worker].append(gant_diagram[iter_number][worker])

    return rotate_diagram


def level_strategy(pred_task_table: list, next_task_table: list, worker_count: int):
    # Длинна таблицы
    table_length = len(next_task_table)

    # Связи между предками и потомками
    relations = {}

    # Корни дерева
    roots = []

    # Создаём словарь связей между pred и next
    for i in range(table_length):
        next = next_task_table[i]
        pred = pred_task_table[i]

        # Для каждого предка указываем потомков
        if next not in relations.keys():
            # Если список ещё не создан, создаём его
            relations[next] = []

        relations[next].append(pred)

        # Ищем корни (вершины, не имеющие предков)
        if next not in pred_task_table:
            if next not in roots:
                roots.append(next)

    print('Relations:')
    pprint(relations)

    print('\nRoots:', roots, '\n')

    # Перевёрнутый список работ
    reversed_works = fill_task_on_graph(relations, roots)

    # Список работ
    works = reversed_works.copy()
    works.reverse()

    print(works, '\n')

    # Строим диаграмму Ганта
    pprint(create_gantt_diagram(relations, works, worker_count), width=40)


def lex_level_strategy(pred_task_table: list, next_task_table: list, worker_count: int):
    # Длинна таблицы
    table_length = len(next_task_table)

    # Связи между предками и потомками
    relations = {}

    # Корни дерева
    roots = []

    # Создаём словарь связей между pred и next
    for i in range(table_length):
        next = next_task_table[i]
        pred = pred_task_table[i]

        # Для каждого предка указываем потомков
        if next not in relations.keys():
            # Если список ещё не создан, создаём его
            relations[next] = []

        relations[next].append(pred)

        # Ищем корни (вершины, не имеющие предков)
        if next not in pred_task_table:
            if next not in roots:
                roots.append(next)

    print('Relations:')
    pprint(relations)

    print('\nRoots:', roots, '\n')

    # Связи между предками и потомками
    reversed_relations = {}

    # Создаём словарь связей между next и pred
    for i in range(table_length):
        next = next_task_table[i]
        pred = pred_task_table[i]

        # Для каждого предка указываем потомков
        if pred not in reversed_relations.keys():
            # Если список ещё не создан, создаём его
            reversed_relations[pred] = []

        reversed_relations[pred].append(next)

    print('Reversed relations:')
    pprint(reversed_relations)

    # Перевёрнутый список работ
    reversed_works = fill_task_on_graph_lex(relations, reversed_relations, roots)

    # Список работ
    works = reversed_works.copy()
    works.reverse()

    print('\n', works, '\n')

    # Строим диаграмму Ганта
    pprint(create_gantt_diagram(relations, works, worker_count), width=50)


if __name__ == '__main__':
    print(find_transit_ways(pred_task_table_lex, next_task_table_lex))

    # level_strategy(pred_task_table_lev, next_task_table_lev, worker_count_lev)

    #lex_level_strategy(pred_task_table_lex, next_task_table_lex, worker_count_lex)

    # create_print_graphs(pred_task_table_lev, next_task_table_lev)

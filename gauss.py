from math import prod
import random
from statistics import mean
import time
from decimal import Decimal
import numpy as np


def subtract(a, b):
	if len(a) != len(b):
		raise Exception()
	else:
		return [a_i - b_i for a_i, b_i in zip(a, b)]


def move_row(matrix, old: int, new: int):
    if 0 > old > len(matrix):
        raise ValueError(old)
    if new > len(matrix):
        raise ValueError(new)
    matrix[old], matrix[new] = matrix[new], matrix[old]
    return matrix


def decimal_matrix(matrix):
	new_matrix = []
	for row in matrix:
		new_matrix.append([Decimal(i) for i in row])
	return new_matrix


def count_row_perm_num(matrix1, matrix2):
	if len(matrix1) != len(matrix2):
		raise Exception()
	if sorted(matrix1) != sorted(matrix2):
		raise Exception()
	perms = 0
	while matrix1 != matrix2:
		...
	return perms


def bubble_sort(arr):
    # num_comp = 0
    num_moves = 0
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(0, len_arr - 1 - i):
            # num_comp += 1
            if arr[j] > arr[j + 1]:
                num_moves += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, num_moves


def shift_zero_rows_down(matrix):
	'''Возврат:\n
	new_matrix, num_moves
	'''
	new_matrix = []
	for row in matrix:
		zeros_num = 0
		for i in row:
			if i == 0:
				zeros_num += 1
			else:
				break
		new_matrix.append((zeros_num, row))
	r_matrix, num_moves = bubble_sort(new_matrix)
	new_matrix = [i[1] for i in r_matrix]
	return new_matrix, num_moves


def find_det_via_gauss(matrix):
	# matrix = decimal_matrix(matrix)
	len_ = range(len(matrix)) # Размер матрицы
	divisors = []
	for col in range(len(matrix)-1):
		# Строка с диагоньним числом, которую будем вычитать из ненулевых строк
		subtrahend = None
		
		# Если число на диагонали равно 0, то пытаемся сместить нулевые строки вниз
		if matrix[col][col] == 0:
			matrix, num_moves = shift_zero_rows_down(matrix)
			# При одной перестановке коэффиценты умножаются на -1
			divisors.append((-1)**num_moves)
			# Если всё равно 0, то нет смысла дальше считать, тк все остальные тоже 0
			if matrix[col][col] == 0:
				continue

		for row in len_:
			# Не приводим к единице числа выше диагонали
			if row < col:
				continue
			# Если строка нулевая (не с диагональным числом), то просто её пропускаем
			if matrix[row][col] == 0:
				continue

			# Приводимое число к единице: на которое делим всю строку, чтобы само это число стало единицей
			reduced_to_1 = matrix[row][col]
			# Запоминаем "коэффицент" на который делили всю строку
			divisors.append(reduced_to_1)
			# Делим всю строку на значение той цифры, которая станет 1
			matrix[row] = [n / reduced_to_1 for n in matrix[row]]
			# Если строка с диагонаьным числом, то продолжаем и работаем с другими строками
			if row == col:
				subtrahend = matrix[col]
				continue
 
			matrix[row] = subtract(matrix[row], subtrahend)

	det = prod([matrix[i][i] for i in len_]) * prod(divisors)
	return det



def delete_row_and_column(matrix, column):
    """Удаление столбца и строки, в которых расположен элемент"""

    mat_size = len(matrix) - 1

    # Создаём пустую матрицу
    new_matrix = np.zeros((mat_size, mat_size), dtype=float)

    for str_num in range(mat_size):
        for col_num in range(mat_size):
            if col_num >= column:
                # Переписываем, начиная со 2 строки и следующего стобца
                new_matrix[str_num][col_num] = matrix[str_num + 1][col_num + 1]

            else:
                # Переписываем, начиная со 2 строки
                new_matrix[str_num][col_num] = matrix[str_num + 1][col_num]

    return new_matrix


def find_determinant_last(matrix, size):
    """Поиск определителя"""

    if size == 1:
        return matrix[0, 0]

    elif size == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    else:
        # Знак
        degree = 1

        # Определитель
        det = 0

        # Перебираем все столбцы
        for column in range(size):

            # Обрезаем строку и столбец
            new_matrix = delete_row_and_column(matrix, column)

            if len(new_matrix) == 2:
                det += degree * matrix[0, column] * (
                        new_matrix[0, 0] * new_matrix[1, 1] - new_matrix[0, 1] * new_matrix[1, 0])
            else:
                det += degree * matrix[0, column] * find_determinant_last(new_matrix, size - 1)

            # Меняем знак
            degree = -degree

        del new_matrix

        return det



if __name__ == '__main__':
	n = int(input('Кол-во тестов: '))
	success = 0 
	times = []
	for i in range(n):
		rand_size = np.random.randint(4, 8)
		rand_matrix = np.random.randint(-50, 50, size=(rand_size, rand_size))
		
		start = time.perf_counter()
		det1 = round(find_det_via_gauss(rand_matrix.tolist()))
		end = time.perf_counter()

		det2 = round(find_determinant_last(rand_matrix, rand_size))

		times.append(end-start)

		if det1 != det2:
			print(f'== Тест №{i+1} ==')
			print(rand_matrix)
			print(f'{det1=}')
			print(f'{det2=}')
			print(f'Time: {end-start}')
			print('=================================\n')
		else:
			success += 1
	print(f'Accuracy={success/n*100}%: {success}/{n}')
	print(f'Average time: {mean(times)}')

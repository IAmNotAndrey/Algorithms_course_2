from statistics import mean
import numpy as np
import copy
import time


def delete_row_and_col(matrix, pos):
	new_matrix = copy.deepcopy(matrix)
	row, col = pos
	if row != None:
		_ = new_matrix.pop(row)
	if col != None:
		for i in range(len(new_matrix)):
			_ = new_matrix[i].pop(col)
	return new_matrix


def rec_tridiag_det(matrix):
	if matrix in [[], None]:
		return 0
	if len(matrix) == 1 and len(matrix[0]) == 1:
		return matrix[0][0]
	return matrix[0][0] * rec_tridiag_det(delete_row_and_col(matrix, (0,0))) - matrix[0][1] * rec_tridiag_det(delete_row_and_col(matrix, (0,1)))


def tridiag_matrix(size):
	buf = np.zeros((size, size))
	flat = buf.ravel()
	min_ = -10
	max_ = 10
	# Рандомные числа в диагоналях
	flat[0::size+1] = np.random.randint(min_, max_, size)
	flat[size::size+1] = np.random.randint(min_, max_, size-1)
	flat[1::size+1] = np.random.randint(min_, max_, size-1)
	# # Одинаковые числа в диагоналях
	# flat[0::size+1] = np.random.randint(min_, max_)
	# flat[size::size+1] = np.random.randint(min_, max_)
	# flat[1::size+1] = np.random.randint(min_, max_)
	# flat[0::size+1] = 6
	# flat[size::size+1] = 1
	# flat[1::size+1] = 9
	
	return buf


def iter_tridiag_det(matrix):
	if matrix in [[], None]:
		return 0
	if len(matrix) == 1:
		return matrix[0][0]
	elif len(matrix) == 2:
		return matrix[0][0]**2 - matrix[0][1]*matrix[1][0]

	# n_m_1 = matrix[0][0]**2 - matrix[0][1]*matrix[1][0]
	# n_m_2 = matrix[0][0]

	# for _ in range(len(matrix)-2):
	# 	n = matrix[0][0]*n_m_1 - matrix[0][1]*matrix[1][0]*n_m_2
	# 	n_m_2 = n_m_1
	# 	n_m_1 = n

	det_n_m_2 = 0
	det_n_m_1 = 1
	for n in range(len(matrix)):
		det_n = matrix[n][n]*det_n_m_1 - matrix[n][n-1]*matrix[n-1][n]*det_n_m_2
		det_n_m_2 = det_n_m_1
		det_n_m_1 = det_n
	
	return det_n_m_1


if __name__ == '__main__':
	success = 0
	rec_triag_times = []
	iter_triag_times = []
	n = int(input('Количество тестов: '))
	for i in range(n):
		matrix = tridiag_matrix(5).tolist()

		start = time.perf_counter()
		rec_triag = rec_tridiag_det(matrix)
		end = time.perf_counter()
		rec_triag_times.append(end-start)

		start = time.perf_counter()
		iter_triag = iter_tridiag_det(matrix)
		end = time.perf_counter()
		iter_triag_times.append(end-start)

		print(np.array(matrix))

		if rec_triag != iter_triag:
			print(f'== Тест №{i+1} ==')
			print(np.array(matrix))
			print(f'{rec_triag=}')
			print(f'{iter_triag=}')
			print(f'Rec time={rec_triag_times[-1]}')
			print(f'Iter time={iter_triag_times[-1]}')
			print('=================================\n')
		else:
			success += 1

	print(f'Accuracy={success / n * 100}%: {success}/{n}')
	print(f'Average rec time:  {mean(rec_triag_times)}')
	print(f'Average iter time: {mean(iter_triag_times)}')

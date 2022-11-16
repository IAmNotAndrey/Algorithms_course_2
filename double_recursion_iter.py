from statistics import mean
import time
import numpy as np
import double_recursion_rec as dr


def num_of_combs_via_td_matrix(n, k):
	if n < k:
		raise Exception('n < k')
	if n < 0 or k < 0:
		raise Exception('n or k < 0')

	if k == 0 or k == n:
		return 1
	elif k == 1:
		return n

	if n == 0 and k != 0:
		return 0

	matrix = np.zeros((k+1, n+1))
	np.fill_diagonal(matrix, 1)
	matrix[0] = 1
	for col in range(n+1):
		matrix[1][col] = col

	for row in range(k+1):
		try:
			matrix[row][row+1] = row + 1
		except IndexError:
			continue

	if matrix[k][n] != 0:
		return matrix[k][n]

	k_cur = 2
	n_cur = 4
	for row in range(k-1):
		n_cur_local = n_cur

		c_left_up = matrix[k_cur-1][n_cur_local-1]
		c_left = matrix[k_cur][n_cur_local-1]

		for col in range(n-k-1):
			matrix[k_cur][n_cur_local] = c_left_up + c_left
			c_left = matrix[k_cur][n_cur_local]
			n_cur_local += 1
			c_left_up = matrix[k_cur-1][n_cur_local-1]

		k_cur += 1
		n_cur += 1

	return matrix[k][n]


def num_of_combs_via_od_matrix(n, k):
	if n < k:
		raise Exception('n < k')
	if n < 0 or k < 0:
		raise Exception('n or k < 0')

	if k == 0 or k == n:
		return 1
	elif k == 1:
		return n

	if n == 0 and k != 0:
		return 0

	num_of_combs = 1
	while k > 0:
		num_of_combs *= n / k
		k -= 1
		n -= 1

	return num_of_combs


if __name__ == '__main__':
	task = int(input('1.Тесты\n2.Проверка скорости итерации и рекурсии\n'))
	test_num = int(input('Кол-во тестов = '))

	success_num = 0
	iter_td_times = []
	iter_od_times = []
	rec_times = []

	for _ in range(test_num):
		k = np.random.randint(0, 50)
		n = k + np.random.randint(0, 20)

		start = time.perf_counter()
		a = num_of_combs_via_td_matrix(n, k)
		end = time.perf_counter()
		iter_td_times.append(end-start)

		start = time.perf_counter()
		c = num_of_combs_via_od_matrix(n, k)
		end = time.perf_counter()
		iter_od_times.append(end-start)

		start = time.perf_counter()
		b = dr.recur_relation(n, k)
		end = time.perf_counter()
		rec_times.append(end-start)

		# Рекурсивный алгоритм сбивает точность, поэтому создано данное условие
		if abs(dr.recur_relation(n, k) - num_of_combs_via_od_matrix(n, k)) <= 0.1 \
			and abs(dr.recur_relation(n, k) - num_of_combs_via_td_matrix(n, k)) <= 0.1:
			success_num += 1
		else:
			print(f'{n=}, {k=}')
			print(f'iter_od={c}')
			print(f'iter_td={a}')
			print(f'rec={b}')
			print()

	match task:
		case 1:
			print(f'Success tests:{success_num}/{test_num}')
			print(f'Accuracy:{success_num/test_num*100}%')

		case 2:
			print(f'Iter od mean time = {mean(iter_od_times)}')
			print(f'Iter td mean time = {mean(iter_td_times)}')
			print(f'Rec mean time = {mean(rec_times)}')
			print(f'Fastest: {min(mean(iter_od_times), mean(iter_td_times), mean(rec_times))}')

		case _:
			print('Не то вы нажали .__.')

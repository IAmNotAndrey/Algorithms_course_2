from pprint import pprint
import random
from math import inf
from tabulate import tabulate


def tape_strategy(works: list, worker_num: int):
	HIGHEST_WORKER_NUM = inf
	
	# Проверка корректности ввода параметра worker_num
	if worker_num <= 0:
		raise ValueError('worker_num <= 0')
	elif worker_num > HIGHEST_WORKER_NUM:
		raise ValueError('worker_num > HIGHEST_WORKER_NUM')
	if not isinstance(worker_num, int):
		raise TypeError(f'worker_num must be int, not {type(worker_num)}')

	# Проверка корректности ввода параметра works
	if len(works) == 0:
		raise ValueError('works length <= 0')
	if not isinstance(works, list):
		raise TypeError(f'works must be list, not {type(works)}')
	if not all(isinstance(x, (int, float)) for x in works):
		raise TypeError('works elements must be int or float')
	if not all(x > 0 for x in works):
		raise ValueError('works elements must be > 0')

	# # Дополнительный элемент для нахождения оптимального времени
	# extra_elem = None
	# # Оптимальное время
	# t_opt = None
	
	# Дополнительный элемент для нахождения оптимального времени
	extra_elem = sum(works) / worker_num
	# Оптимальное время
	t_opt = max([max(works), extra_elem])
	
	# Проверку на возможность сократить количество рабочих без увеличения оптимального времени
	while True:
		next_extra_elem = sum(works) / (worker_num-1)
		next_t_opt = max([max(works), next_extra_elem])
		# Если оптимальное время не меняется, то уменьшаем количество рабочих
		if t_opt >= next_t_opt:
			worker_num -= 1
			t_opt = next_t_opt
		else:
			break

	# Подготовленная разрезанная лента
	cut_tape = [[] for _ in range(worker_num)]

	global operation_count
	operation_count = 0


	def rec(work_index, passed_time, work_time, worker_index):
		"""
		Рекурсивная функция для удобного заполнения ленты без потери нужной информации

		work_index : индекс работы
		passed_time : отработанное текущим рабочим время
		work_time : время, которое текущий рабочий собирается отработать
		worker_index : индекс текущего рабочего
		"""

		global operation_count
		operation_count += 1

		sum_time = passed_time + work_time
		if sum_time > t_opt:
			next_time = sum_time - t_opt
			cur_time = work_time - next_time
			
			cut_tape[worker_index].append({work_index: round(cur_time, 2)})
			
			rec(work_index, 0, next_time, worker_index+1)
			
		elif sum_time == t_opt:
			cut_tape[worker_index].append({work_index: round(work_time, 2)})
			try:
				rec(work_index+1, 0, works[work_index+1], worker_index+1)
			except IndexError:
				return

		else:
			cut_tape[worker_index].append({work_index: round(work_time, 2)})
			try:
				rec(work_index+1, sum_time, works[work_index+1], worker_index)	
			except IndexError:
				return

	rec(0, 0, works[0], 0)

	return cut_tape, t_opt, worker_num, operation_count


if __name__ == '__main__':
	
	test_number = 1

	if test_number == 0:
		# works = [5, 2, 4, 3, 7, 6]
		# workers_number = 3

		# works = [3,4,6,7,7,9,10,12,17]
		# workers_number = 5

		# works = [3.123124,4.56548,6.626058,7.65405664,7.568405,9.056,10.56,12,17.6512]
		# workers_number = 5

		works = [5, 4, 4, 3, 7, 10]
		workers_number = 3

		result = tape_strategy(works, workers_number)

		print('\nWorkers count:', result[2])
		print('Min time:', result[1], '\n')
		print('O(n):', result[3])

		pprint(
			result[0],
			depth=24,
			width=40
		)

		print('\nResult:')

		result_matrix = []

		for worker in result[0]:
			result_matrix.append([])

			for task in worker:

				current_key = int(list(task.keys())[0])
				current_value = int(list(task.values())[0])

				for i in range(current_value):
					result_matrix[-1].append(current_key + 1)

		print(tabulate(result_matrix, headers=range(int(result[1])), tablefmt='orgtbl'))

	else:
		time_tasks = []

		for task_count in range(5, 100):
			tasks_length = []

			for i in range(task_count):
				tasks_length.append(10)

			time_tasks.append(tape_strategy(tasks_length, 5)[3])

		print(time_tasks)
		print()
		new_time_tasks = [*time_tasks[1:]]

		for i in range(len(new_time_tasks)):
			new_time_tasks[i] = new_time_tasks[i] - time_tasks[i]

		print(new_time_tasks)

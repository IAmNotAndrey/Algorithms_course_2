from pprint import pprint
import random
from math import inf


def tape_strategy(works: list, worker_num: int):
	HIGHEST_WORKER_NUM = inf
	
	# Проверка корректности ввода параметра worker_num
	if worker_num <= 0:
		raise ValueError('worker_num <= 0')
	elif worker_num > HIGHEST_WORKER_NUM:
		raise ValueError('worker_num >= HIGHEST_WORKER_NUM')
	# ! Выдаёт ошибку постоянно, мол число не int. Явное приведение к int при вводе параметров также не помогает
	# if not isinstance(works, int):
	# 	raise TypeError(f'worker_num must be int, not {type(worker_num)}')

	# Проверка корректности ввода параметра works
	if len(works) == 0:
		raise ValueError('works length <= 0')
	if not isinstance(works, list):
		raise TypeError(f'works must be list, not {type(works)}')
	if not all(isinstance(x, int | float) for x in works):
		raise TypeError('works elements must be int or float')
	if not all(x > 0 for x in works):
		raise ValueError('works elements must be > 0')

	# Дополнительный элемент для нахождения оптимального времени
	extra_elem = None
	# Оптимальное время
	t_opt = None
	
	# Проверку на возможность сократить количество рабочих без увеличения оптимального времени
	pre_t_opt = None
	while True:
		extra_elem = sum(works) / worker_num
		t_opt = max([max(works), extra_elem])
		# Хотя бы 1 раз выполняем цикл
		if pre_t_opt == None:
			worker_num -= 1
			pre_t_opt = t_opt
			continue
		# Если оптимальное время не меняется, то уменьшаем количество рабочих
		if t_opt == pre_t_opt:
			worker_num -= 1
		else:
			break
	# Подготовленная разрезанная лента
	cut_tape = [[] for _ in range(worker_num)]

	def rec(work_index, passed_time, work_time, worker_index):
		'''
		Рекурсивная функция для удобного заполнения ленты без потери нужной информации
		
		work_index : индекс работы
		passed_time : отработанное текущим рабочим время
		work_time : время, которое текущий рабочий собирается отработать
		worker_index : индекс текущего рабочего
		'''
		sum_time = passed_time + work_time
		if sum_time > t_opt:
			next_time = sum_time - t_opt
			cur_time = work_time - next_time
			
			cut_tape[worker_index].append({work_index: cur_time})
			
			rec(work_index, 0, next_time, worker_index+1)
			
		elif sum_time == t_opt:
			cut_tape[worker_index].append({work_index: work_time})
			try:
				rec(work_index+1, 0, works[work_index+1], worker_index+1)
			except IndexError:
				return

		else:
			cut_tape[worker_index].append({work_index: work_time})
			try:
				rec(work_index+1, sum_time, works[work_index+1], worker_index)	
			except IndexError:
				return

	rec(0, 0, works[0], 0)

	return cut_tape


if __name__ == '__main__':
	# Тесты
	test_num = int(input())
	for i in range(test_num):
		work_num = random.randint(2, 20)
		works = []
		for _ in range(work_num):
			works.append(random.randint(2, 50)*random.random())

		worker_num = random.randint(2, 10)
		print(
			i,
			tape_strategy(works, int(worker_num))
		)

	# print(
	# 	tape_strategy(
	# 		[5,2,4,3,7,6], 10,
	# 	)
	# )
	
from pprint import pprint


def johnson_algorithm(tasks:list[list]) -> tuple:
	'''Реализует алгоритм Джонсона
	
	Возвращает :
		оптимальное время выполнения задач,
		диаграмму ганта
	'''
	
	# Группа задача, где a_i <= b_i
	group_1_tasks = []
	# Группа задача, где a_i > b_i
	group_2_tasks = []

	# Группировка задач по группам с сохранением их индекса
	for i, task in enumerate(tasks):
		if task[0] <= task[1]:
			group_1_tasks.append([i, task])
		else:
			group_2_tasks.append([i, task])

	# Сортировка первой группы по возрастанию a_i
	group_1_tasks.sort(key=lambda x: x[1][0])
	# Сортировка первой группы по убыванию b_i
	group_2_tasks.sort(key=lambda x: x[1][1], reverse=True)
	# Объединение групп для удобства использования
	sorted_tasks = group_1_tasks + group_2_tasks
	
	# Диаграмма Ганта для 1-го и 2-го исполнителя
	gantt_chart = [[], []]

	# Заполнение 1-го исполнителя
	time = 0
	for task in sorted_tasks:
		# Длительность выполнения задания : (нач.время, кон.время)
		duration = [time]
		time += task[1][0]
		# Добавление кон.времени
		duration.append(time)
		# Добавление задачи для 1-го исполнителя в формате : [index, [start_time, end_time]]
		gantt_chart[0].append([task[0], duration])
		
	
	# Заполнение 2-го исполнителя
	# Начальное время = кон.время первой задачи
	time = gantt_chart[0][0][1][1]
	# Здесь используем заполненную часть диаграммы Ганта
	for task in gantt_chart[0]:
		# Если текущее время < кон.время этого же задания для 1-го исполнителя...
		if time < task[1][1]:
			time = task[1][1]

		# По аналогии с заполнением 1-го исполнителя
		duration = [time]
		# time += b_i
		time += tasks[task[0]][1]
		duration.append(time)
		
		gantt_chart[1].append([task[0], duration])

	# Оптимальное время = кон.время последней задачи для 2-го исполнителя
	return gantt_chart[1][-1][1][1], gantt_chart


if __name__ == '__main__':
	# # Тесты
	# from random import randint 
	# test_num = 10000
	# for _ in range(test_num):
	# 	task_num = randint(2, 20)
	# 	tasks = [[randint(1, 20), randint(1, 20)] for _ in range(task_num)]
	# 	johnson_algorithm(tasks)

	# Задача из тетради (кр)
	tasks = [
		[4,3],
		[5,2],
		[3,5],
		[2,3],
		[4,4],
		[7,6],
		[1,2],
	]

	# # Задача из презентации
	# tasks = [
	# 	[7,2],
	# 	[3,4],
	# 	[2,5],
	# 	[4,1],
	# 	[6,6],
	# 	[5,3],
	# 	[4,5],
	# ]

	pprint(
		johnson_algorithm(tasks)
	)

# * Пример взят из 3-го варианта кр 2 модуля 

# Задания вводятся списком кортежей (пред.задание:посл.задание)
# ! Удаляет повторяющиеся значения
tasks = list(zip(
	list('AAACCDDFFFHHHII'),
	list('EGJFHBJADGBEIGJ'),
))


def level_strategy(tasks:list[tuple], worker_num: int):
	# Нахождение всех уникальных названий заданий
	# TODO: Возможны '-' в качестве отсутствия задачи
	unique_task_names = sorted(set([item for sublist in tasks for item in sublist]))
	task_name_priorities = [None for _ in range(len(unique_task_names))]
	
	# 0-й уровень, или база, находится путём поиска отсутствующих заданий в строке пред.задания
	base = set([missing for missing in unique_task_names 
	if missing not in set([elem[0] for elem in tasks])])
	
	# Дерево связей
	relations = [set() for _ in range(len(unique_task_names))]
	
	def rec(passed_tasks:set, level_tasks:set):
		'''Создаёт дерево отношений'''

		# Если set_ пустой, значит мы достигли вершины дерева
		if len(level_tasks) == 0: 
			return
		
		unique_level_tasks = set()
		
		for elem in tasks:
			if elem[1] in level_tasks:
				# Запоминаем вершины текущего уровня
				unique_level_tasks.add(elem[0])
				
				# TODO: удалить транзитивные дуги
				for passed_task in passed_tasks:
					relations[unique_task_names.index(passed_task)].discard(elem[0])
					
				relations[unique_task_names.index(elem[1])].add(elem[0])

		rec(passed_tasks.union(level_tasks), unique_level_tasks)

	# # Установка приоритетов для base-элементов в проивольном порядке
	# for i, task in enumerate(base):
	# 	task_name_priorities[unique_task_names.index(task)].add(i)
	
	# def set_priorities(set_:set):
	# 	'''Устанавливает приоритеты для задач'''
	# 	for task in set_:


	rec(set(), base)
	print(relations)



level_strategy(tasks, None)

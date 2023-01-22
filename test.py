from copy import copy
import random


def best_investment(investments_: list, project_matrix_: list[list]):
	investments: list = sorted(copy(investments_))
	project_matrix: list = sorted(copy(project_matrix_))
	
	# Число предприятий, в которые осуществляется инвестирование, начиная с нулевого
	m = len(project_matrix[0])
	# Ряд разложения инвестиций
	investments_num = len(investments)
	# Таблица условной оптимизации
	table = [{'x': [0]*(investments_num), 'W':[0]*(investments_num)} for _ in range(m)]

	def investments_index(x):
		return investments.index(x)

	def fi(i, x):
		if x == 0:
			return 0
		return project_matrix[investments.index(x)][i]

	def W(i, s):
		# Возврат: (max(W), x)
		if i == m-1:
			return fi(i, s), s

		if s == 0:
			return 0, 0

		W_variants = []
		for x in investments:
			if s >= x:
				W_result = fi(i, x) + W(i+1, s-x)[0]
				W_variants.append([W_result, x])
		return max(W_variants)
		# try:
		# 	return max(W_variants)
		# except ValueError:
		# 	return 0

	for i in reversed(range(m)):	
		if i == 0:
			s_ = investments[-1]
			index = investments_index(s_)
			W_result, x_result = W(i, s_)
			table[i]['x'][-1] = x_result
			table[i]['W'][-1] = W_result
			break
			
		for s in investments:
			if i == m-1:
				index = investments_index(s)
				table[i]['x'][index] = s
				table[i]['W'][index] = fi(i, s)
			
			else:
				index = investments_index(s)
				W_result, x_result = W(i, s)
				table[i]['x'][index] = x_result
				table[i]['W'][index] = W_result

	distribution = []
	# Безусловная оптимизация
	cur_s = investments[-1]
	cur_x = None
	for i, row in enumerate(table):
		if i == 0:
			_, x = max(zip(row['W'], row['x']))
			cur_x = x
		else:
			cur_s -= cur_x
			if cur_s == 0:
				distribution.append(0)
				continue
			x = row['x'][investments_index(cur_s)]
			cur_x = x
		distribution.append(x)
	
	return table[0]['W'][-1], distribution


# def random_project_matrix_and_investment(num_of_companies: int, num_of_investments: int) -> tuple[list[list], list]:
# 	'''
# 	:param num_of_companies: number of companies >= 2
# 	:param num_of_investments: number of investments >= 2
# 	:return: random generated project matrix and investmants list
# 	'''
# 	investment_start = random.randint(1, 10)
# 	investment_step = random.randint(1, 10)
# 	investments = []
# 	for i in range(num_of_companies):
# 		investments.append(investment_start)
# 		investment_start += investment_step
	
# 	project_matrix = [[None]*num_of_investments for _ in range(num_of_companies)]
# 	for company in project_matrix:
# 		start = random.randint(1, 10)
# 		step = random.randint(1, 10)
# 		for ind, _ in enumerate(company):
# 			company[ind] = start
# 			start += step
# 	# Транспонирование матрицы
# 	project_matrix = list(map(list, zip(*project_matrix)))

# 	return project_matrix, investments



if __name__ == '__main__':
	# investments = [10, 20, 30, 40, 50]
	investments = [1, 2, 3, 4, 5]
	# investments = [1, 2, 3]

	# project_matrix = [
	# 	[11, 13, 14, 12],
	# 	[15, 17, 19, 21],
	# 	[22, 25, 28, 31],
	# 	[36, 32, 40, 44],
	# 	[51, 54, 53, 52],
	# ]
	project_matrix = [
		[1.5, 2, 1.7],
		[2, 2.1, 2.4],
		[2.5, 2.3, 2.7],
		[3, 3.5, 3.2],
		[3.6, 4, 3.5],
	]
	# project_matrix = [
	# 	[2,3,2],
	# 	[4,5,7],
	# 	[6,8,8],
	# ]

	# project_matrix, investments = random_project_matrix_and_investment(5, 5)

	max_profit, distribution = best_investment(investments, project_matrix)
	print(f'{max_profit=}')
	print(f'{distribution=}')

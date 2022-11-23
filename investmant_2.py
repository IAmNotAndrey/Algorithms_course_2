from copy import deepcopy
import numpy as np


investments = [0, 1, 2, 3]

project_matrix = [
	[0, 0, 0],
	[2, 3, 2],
	[4, 5, 7],
	[6, 8, 8],
]
# Транспонируем матрицу для удобства использования
project_matrix = list(map(list, zip(*project_matrix)))

def best_investments(investments, project_matrix):
	investments = deepcopy(investments)
	project_matrix = deepcopy(project_matrix)
	
	investments_num = len(investments)
	project_matrix_num = len(project_matrix)
	
	# Берём первые 2 строчки при инвестиции 1 и 2 единиц для n проектов
	A = project_matrix[0]
	B = project_matrix[1]

	funcs_list_list = []

	for _ in range(project_matrix_num-1):
		matrix = np.zeros((investments_num, investments_num)).tolist()
		
		funcs_list = np.empty((investments_num, 0)).tolist()
		
		for a in range(investments_num):
			for b in range(investments_num - a):
				matrix[a][b] = A[a] + B[b]
				funcs_list[a+b].append((matrix[a][b], {a: A[a], b: B[b]}))
		
		funcs_list_list.append(funcs_list)
		
		# Находим максимумы
		max_funcs = []
		for funcs in funcs_list:
			local = []
			for func in funcs:
				local.append(func[0])
			max_funcs.append(max(local))
		
		del project_matrix[0]
		project_matrix[0] = max_funcs
		A = deepcopy(project_matrix[0])
		try:
			B = deepcopy(project_matrix[1])
		except IndexError:
			pass
	return max(A)

if __name__ == '__main__':
	print(
		best_investments(investments, project_matrix)
	)

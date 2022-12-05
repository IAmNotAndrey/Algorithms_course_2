from itertools import product
from pprint import pprint


class TriangleWays():
	def __init__(self, steps: int, matrix: list, start_point: str ='a'):
		self.steps = steps
		self.start_point = start_point
		self.is_AA = True if (matrix[0][3] in [1]) else False
		self.is_AB = True if (matrix[0][0] in [1] and matrix[1][0] in [-1, 1]) else False
		self.is_BA = True if (matrix[1][0] in [1] and matrix[0][0] in [-1, 1]) else False
		self.is_BC = True if (matrix[1][1] in [1] and matrix[2][1] in [-1, 1]) else False
		self.is_CB = True if (matrix[2][1] in [1] and matrix[1][1] in [-1, 1]) else False
		self.is_AC = True if (matrix[0][2] in [1] and matrix[2][2] in [-1, 1]) else False
		self.is_CA = True if (matrix[2][2] in [1] and matrix[0][2] in [-1, 1]) else False

	def is_segment_valid(self, segment: str) -> bool:
		''' Функция проверки на возможность существования отрезка, исходя из условий'''
		is_valid = not (
			# (segment[0] == segment[1]) # 'aa', 'bb' или 'cc'
			((segment[0] == segment[1]) and (segment[0] not in ['a']) and (segment[1] not in ['a']))
			or (segment[0] in ['a'] and segment[1] in ['a'] and not self.is_AA)
			or (segment[0] in ['a'] and segment[1] in ['b'] and not self.is_AB) 
			or (segment[0] in ['b'] and segment[1] in ['a'] and not self.is_BA) 
			or (segment[0] in ['b'] and segment[1] in ['c'] and not self.is_BC) 
			or (segment[0] in ['c'] and segment[1] in ['b'] and not self.is_CB) 
			or (segment[0] in ['a'] and segment[1] in ['c'] and not self.is_AC) 
			or (segment[0] in ['c'] and segment[1] in ['a'] and not self.is_CA) 
		)
		return is_valid

	def find_all_ways(self):
		ways = []
		def next_available_point(pre_path: str, n):
			if n < self.steps:
				if self.is_segment_valid(pre_path[-1]+'a'):
					next_available_point(pre_path+'a', n+1)			
				if self.is_segment_valid(pre_path[-1]+'b'):
					next_available_point(pre_path+'b', n+1)			
				if self.is_segment_valid(pre_path[-1]+'c'):
					next_available_point(pre_path+'c', n+1)			
			else:
				ways.append(pre_path)

		next_available_point(self.start_point, 0)
		return ways


def ways_in_triangle(matrix, n):
	'''matrix - матрица инциденций\n
	n - количество шагов
	'''
	
	is_AA = True if (matrix[0][3] in [1]) else False
	is_AB = True if (matrix[0][0] in [1] and matrix[1][0] in [-1, 1]) else False
	is_BA = True if (matrix[1][0] in [1] and matrix[0][0] in [-1, 1]) else False
	is_BC = True if (matrix[1][1] in [1] and matrix[2][1] in [-1, 1]) else False
	is_CB = True if (matrix[2][1] in [1] and matrix[1][1] in [-1, 1]) else False
	is_AC = True if (matrix[0][2] in [1] and matrix[2][2] in [-1, 1]) else False
	is_CA = True if (matrix[2][2] in [1] and matrix[0][2] in [-1, 1]) else False
	
	points = list('abc')
	ways = []

	def is_segment_valid(segment: str) -> bool:
		''' Функция проверки на возможность существования отрезка, исходя из условий'''
		is_valid = not (
			# (segment[0] == segment[1]) # 'aa', 'bb' или 'cc'
			((segment[0] == segment[1]) and (segment[0] not in ['a']) and (segment[1] not in ['a'])) # 'aa', 'bb' или 'cc'
			or (segment[0] in ['a'] and segment[1] in ['a'] and not is_AA)
			or (segment[0] in ['a'] and segment[1] in ['b'] and not is_AB) 
			or (segment[0] in ['b'] and segment[1] in ['a'] and not is_BA) 
			or (segment[0] in ['b'] and segment[1] in ['c'] and not is_BC) 
			or (segment[0] in ['c'] and segment[1] in ['b'] and not is_CB) 
			or (segment[0] in ['a'] and segment[1] in ['c'] and not is_AC) 
			or (segment[0] in ['c'] and segment[1] in ['a'] and not is_CA) 
		)
		return is_valid

	for way in product(points, repeat=n+1):
		do_stop = False # Флаг остановки прохода по пути, если найдётся недопустимый промежуток
		previous_point = ''
		current_point = ''
		for i, point in enumerate(way):
			current_point = point
			segment = previous_point + current_point
			previous_point = current_point
			if i == 0: # Пропускаем отрезок '_(a/b/c)'
				continue
			if not is_segment_valid(segment):
				do_stop = True
				break
		if do_stop:
			continue

		ways.append(way)
	
	return ways
	

if __name__ == '__main__':
	# 	AB	BC	CA	AA
	# A	
	# B	
	# C	
	
	# matrix = [
	# 	[1, 0, 1, 0],
	# 	[0, 1, 0, 0],
	# 	[0, 1, 1, 0],
	# ]
	matrix = [
		[0, 0, 1, 1],
		[0, -1, 0, 0],
		[0, 1, 1, 0],
	]
	n = 5
	ways = ways_in_triangle(matrix, n)
	end_A = 0
	end_B = 0
	end_C = 0
	for way in ways:
		match way[-1]:
			case 'a':
				end_A += 1
			case 'b':
				end_B += 1
			case 'c':
				end_C += 1
	# pprint(ways)
	# print(f'{end_A=}, {end_B=}, {end_C=}')
	print(len(ways))
	
	pprint(TriangleWays(n, matrix, start_point='a').find_all_ways())
	pprint(TriangleWays(n, matrix, start_point='b').find_all_ways())
	pprint(TriangleWays(n, matrix, start_point='c').find_all_ways())


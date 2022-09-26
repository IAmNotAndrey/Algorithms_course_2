import numpy as np
import math
import itertools as it


""" def find_determinant(matrix):
	matrix_len = len(matrix)
	positions = [i for i in range(matrix_len)]
	all_position_combinations = tuple(it.permutations(positions))
	number_of_terms = math.factorial(matrix_len)
	det = 0
		
	for row in all_position_combinations:
		p = count_inversion_num(row)


def count_inversion_num(row) -> int:
	dict_ = {pos: val for pos, val in enumerate(row)}
	combinations = it.permutations(dict_, 2)
	inversion_num = 0
	for i in combinations:
		if get_key(dict_, i[0]) < get_key(dict_, i[1]) and i[0] > i[1]:
			inversion_num += 1
	return inversion_num


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k 


if __name__ == '__main__':
	count_inversion_num((1, 2, 3)) """


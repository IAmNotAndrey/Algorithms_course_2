def perm_iter(arr):
	arr_len = len(arr)
	indexes = [i for i, _ in enumerate(arr)]
	i = 0

	while i < arr_len:
		indexes[i] -= 1

		j = i % 2 * indexes[i]
		arr[i], arr[j] = arr[j], arr[i]

		yield arr
		
		i = 1
		try:
			while indexes[i] == 0:
				indexes[i] = i
				i += 1
		except IndexError:
			break

if __name__ == '__main__':
	for var in perm_iter(list('abc')):
		print(var)

def gcd(a, b):
	greatest = max(a, b)
	smallest = min(a, b)
	if greatest % smallest != 0:
		return gcd(smallest, greatest % smallest)
	else:
		return smallest


def lcm(a, b):
	return a * b / gcd(a, b)


# [!] ТЕСТИТЬ И СТИРАТЬ ПО ЗАВЕРШЕНИИ ЗДЕСЬ
if __name__ == "__main__":
	...
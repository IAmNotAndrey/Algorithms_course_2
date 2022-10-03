import math
from statistics import mean
import time
import numpy as np


def gcd(a, b):
	greatest = max(a, b)
	smallest = min(a, b)
	if greatest % smallest != 0:
		return gcd(smallest, greatest % smallest)
	else:
		return smallest


def lcm(a, b):
	return a * b / gcd(a, b)


def evklid_nod(num1, num2):
    while num1 != 0:
        num1, num2 = num2, num1
        num1 = num1 % num2
    return num2

def factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n / i
        i += 1
    if n > 1:
        factors.append(n)

    return factors

def new_mas(mas1, mas2):
    mas3 = []
    dels = []

    if len(mas1) < len(mas2):
        mas1, mas2 = mas2, mas1

    for n1 in mas1:
        for n2 in mas2:
            if n1 == n2:
                mas3.append(n2)
                dels.append(n1)
                mas2.remove(n2)
                break
    for n in dels:
        mas1.remove(n)
    for n in mas1:
        mas3.append(n)
    for n in mas2:
        mas3.append(n)

    return mas3


def nok(num1, num2):
    mas1 = factorization(num1)
    mas2 = factorization(num2)

    mas3 = new_mas(mas1, mas2)

    mul = math.prod(mas3)

    return mul

# [!] ТЕСТИТЬ И СТИРАТЬ ПО ЗАВЕРШЕНИИ ЗДЕСЬ
if __name__ == "__main__":
	min_value = 1
	max_value = 1000
	
	test_num = int(input('Кол-во тестов: '))

	gcd_success = 0
	lcm_success = 0

	for _ in range(test_num):
		gcd1_times = []
		gcd2_times = []
		lcm1_times = []
		lcm2_times = []

		num1 = np.random.randint(min_value, max_value)
		num2 = np.random.randint(min_value, max_value)

		start = time.perf_counter()
		res1 = gcd(num1, num2)
		end = time.perf_counter()
		gcd1_times.append(end-start)

		start = time.perf_counter()
		res2 = evklid_nod(num1, num2)
		end = time.perf_counter()
		gcd2_times.append(end-start)

		start = time.perf_counter()
		res3 = lcm(num1, num2)
		end = time.perf_counter()
		lcm1_times.append(end-start)

		start = time.perf_counter()
		res4 = nok(num1, num2)
		end = time.perf_counter()
		lcm2_times.append(end-start)

		if res1 == res2:
			gcd_success += 1
		else:
			print(f'ОШИБКА НОД: {num1=}, {num2=}')
			print(f'{res1=}')
			print(f'{res2=}')
			print()

		if res3 == res4:
			lcm_success += 1
		else:
			print(f'ОШИБКА НОК: {num1=}, {num2=}')
			print(f'{res3=}')
			print(f'{res4=}')
			print('\n')
	
	print(f'Точность НОД: {gcd_success}/{test_num}')
	print(f'Ср время рекурсивного НОД:  {mean(gcd1_times)}')
	print(f'Ср время итерационного НОД: {mean(gcd2_times)}')
	print()
	print(f'Точность НОК: {lcm_success}/{test_num}')
	print(f'Ср время рекурсивного НОК:  {mean(lcm1_times)}')
	print(f'Ср время итерационного НОК: {mean(lcm2_times)}')

	
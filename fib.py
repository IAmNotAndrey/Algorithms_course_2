import time


def fib_rec(n):
	if n >= 1:
		if n > 2:
			return fib_rec(n-1) + fib_rec(n-2)
		elif n == 2:
			return 1
		else:
			return 0
	else:
		raise AttributeError("n < 1")

def fib_iter1(n):
	if n >= 1:
		a = 0
		b = 1
		for i in range(n-2):
			c = a
			a = b
			b = a + c
		return b
	else:
		raise AttributeError("n < 1")

# 0 1 1 2 3 5 8 
def fib_iter2(n):
	if n >= 1:
		dif = 1
		a = 0
		for i in range(n-1):
			a += dif
			dif = a - dif
		return a
	else:
		raise AttributeError("n < 1")


start = time.perf_counter_ns()
print(f'res = {fib_rec(30)}')
print(f'eff = {time.perf_counter_ns() - start}')

start = time.perf_counter_ns()
print(f'res = {fib_iter1(30)}')
print(f'eff = {time.perf_counter_ns() - start}')

start = time.perf_counter_ns()
print(f'res = {fib_iter2(30)}')
print(f'eff = {time.perf_counter_ns() - start}')

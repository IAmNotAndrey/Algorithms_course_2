import time
import numpy as np


strings1 = []
strings2 = []
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def ch(pos, chars_list, message=''):
    if pos > 0:
        for char in chars_list:
            new_list = chars_list.copy()
            # Закомментировать, чтобы включить повторения
            new_list.remove(char)

            ch(pos - 1, new_list, message + char)
    else:
        strings1.append(message)


def ch_pov(pos, chars_list, message=''):
    if pos > 0:
        for char in chars_list:
            new_list = chars_list.copy()
            # Закомментировать, чтобы включить повторения
            # new_list.remove(char)

            ch_pov(pos - 1, new_list, message + char)
    else:
        strings2.append(message)


if __name__ == "__main__":
	n = 4
	ch_times = []
	ch_pov_times = []
	
	start = time.perf_counter()
	ch(n, chars)
	end = time.perf_counter()
	ch_times.append(end-start)

	start = time.perf_counter()
	ch_pov(n, chars)
	end = time.perf_counter()
	ch_pov_times.append(end-start)


	# print(strings1)
	print(strings2)
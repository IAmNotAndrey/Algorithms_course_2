strings = []
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def ch(pos, chars_list, message=''):
    if pos > 0:
        for char in chars_list:
            new_list = chars_list.copy()

            # Закомментировать, чтобы включить повторения
            new_list.remove(char)

            ch(pos - 1, new_list, message + char)

    else:
        strings.append(message)


n = 2

ch(n, chars)

print(strings)
print(len(strings))

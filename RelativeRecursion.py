strings = []


def ch_0(n, text=''):
    if n > 1:
        ch_1(n-1, text + '0')
    else:
        strings.append(text + '0')


def ch_1(n, text=''):
    if n > 1:
        ch_0(n-1, text + '1')
        ch_1(n-1, text + '1')
    else:
        strings.append(text+'1')


n = 4

ch_0(n)
ch_1(n)
print(strings)

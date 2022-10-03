n = 7
k = 3


def comb(n, k, n_k):
    if n > 0:
        if k > 0:
            if n_k > 0:
                return n * comb(n - 1, 0, 0) / k * comb(0, k - 1, 0) / n_k * comb(0, 0, n_k - 1)
            else:
                return n * comb(n - 1, 0, 0) / k * comb(0, k - 1, 0)
        elif n_k > 0:
            return n * comb(n - 1, 0, 0) / n_k * comb(0, 0, n_k - 1)
        else:
            return n * comb(n - 1, 0, 0)

    elif k > 0:
        if n_k > 0:
            return 1 / k * comb(0, k - 1, 0) / n_k * comb(0, 0, n_k - 1)
        else:
            return 1 / k * comb(0, k - 1, 0)

    elif n_k > 0:
        return 1 / n_k * comb(0, 0, n_k - 1)

    else:
        return 1


print(comb(n, k, n-k))

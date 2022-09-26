from itertools import permutations

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3


def permutations(elements):
    if len(elements) <= 1:
        yield elements
        return
    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            # nb elements[0:1] works in both string and list contexts
            yield perm[:i] + elements[0:1] + perm[i:]

print([i for i in permutations(nums)])
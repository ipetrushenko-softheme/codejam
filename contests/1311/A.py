def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def min_op(a, b) -> int:
    diff = a - b
    if diff == 0:
        return 0

    if diff > 0:
        is_even = diff % 2 == 0
        if is_even:
            return 1
        else:
            return 2

    diff = -diff
    is_even = diff % 2 == 0
    if is_even:
        return 2
    else:
        return 1


T, = read_ints()
for test in range(T):
    a, b = read_ints()
    print(min_op(a, b))

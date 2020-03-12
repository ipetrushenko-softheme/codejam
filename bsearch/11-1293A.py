def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def compute_min(n, s: int, closed: list):
    l = set(closed)
    m = h = n - 1
    for i in range(s, n + 1):
        if i not in l:
            m = i - s
            break
    for i in range(s, 0, -1):
        if i not in l:
            h = s - i
            break
    return min(m, h)


T, = read_ints()
for test in range(T):
    n, s, k = read_ints()
    closed = read_ints()
    print(compute_min(n, s, closed))
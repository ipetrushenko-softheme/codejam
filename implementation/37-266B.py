def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, t = read_ints()
queue = list(input().strip())


def solve(a: list, t: int) -> int:
    n = len(a)
    for j in range(t):
        i = 0
        while i < n -1:
            if a[i] == 'B' and a[i+1] == 'G':
                a[i], a[i+1] = a[i+1], a[i]
                i = i + 1
            i = i + 1
    return ''.join(a)


print(solve(queue, t))
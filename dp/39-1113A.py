def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, v = read_ints()


def solve(n: int, v: int) -> int:
    if n - 1 < v:
        return n - 1

    if n == v:
        return v

    res = v - 1
    for i in range(1, n - v + 1):
        res += i

    return res


print(solve(n,v))

def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def count(n: int) -> int:
    if n % 2 == 0:
        return n//2 - 1

    return n // 2


T, = read_ints()
for _ in range(T):
    n, = read_ints()
    ans = count(n)
    print(ans)

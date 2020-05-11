def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


T = int(input())


def solve(n: int, k: int) -> int:
    bad = 0
    good = 2*k
    while good - bad > 1:
        m = (good+bad) // 2
        if m - m // n >= k:
            good = m
        else:
            bad = m
    return good


for test in range(T):
    n, k = read_ints()
    ans = solve(n, k)
    print(ans)

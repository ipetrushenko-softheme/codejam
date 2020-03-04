# https://codeforces.com/problemset/problem/1288/A


from math import ceil


def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def f(n: int, d: int) -> bool:
    good = 0
    bad = n

    while bad - good > 1:
        t = (good + bad) // 2
        if good_enough(n, d, t):
            good = t
        else:
            bad = t

    return good_enough(n, d, good)


def good_enough(n: int, d: int, x: int) -> bool:
    new_time = ceil(d / (x+1))
    total = x + new_time
    return total <= n


T, = read_ints()
for _ in range(T):
    n, d = read_ints()
    yes = f(n, d)
    print("YES" if yes else "NO")

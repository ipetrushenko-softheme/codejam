def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


T = int(input())


def solve(a: list) -> int:
    n = len(a)
    pre = [0] * (n+1)
    for l in range(n):
        s = a[l]
        for r in range(l+1, n):
            s += a[r]
            if 0 < s <= n:
                pre[s] += 1

    total = 0
    for i in range(n):
        total += int(pre[a[i]] > 0)
    return total


for test in range(T):
    n, = read_ints()
    arr = read_ints()
    a = solve(arr)
    print(a)

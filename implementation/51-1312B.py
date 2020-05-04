def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


T, = read_ints()


def solve(a: list) -> list:
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if j-i == a[j] - a[i]:
                a[i], a[j] = a[j], a[i]
    return a


for test in range(T):
    n = int(input())
    arr = read_ints()
    ans = solve(arr)
    print(ans)

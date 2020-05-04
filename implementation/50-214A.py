def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, m = read_ints()


def solve(n: int, m: int) -> int:
    k = max(n, m)
    cnt = 0
    for a in range(k+1):
        for b in range(k+1):
            if a*a + b == n and a + b*b == m:
                cnt += 1
    return cnt


print(solve(n, m))

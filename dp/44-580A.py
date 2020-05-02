def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, = read_ints()
arr = read_ints()


def solve(arr: list) -> int:
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            dp[i] = dp[i-1] + 1

    return max(dp)


print(solve(arr))

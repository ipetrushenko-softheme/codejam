def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, = read_ints()
arr = read_ints()


# timeout (1,2,3,4....) in sorted array
# def solve(arr) -> int:
#     n = len(arr)
#     dp = [1] * n
#     for i in range(1, n):
#         j = i
#         count = 1
#         while j > 0 and arr[j-1] < arr[j]:
#             j = j - 1
#             count += 1
#         dp[i] = count
#     return max(dp)


def solve(arr) -> int:
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        if arr[i-1] < arr[i]:
            dp[i] = 1 + dp[i-1]
    return max(dp)


print(solve(arr))
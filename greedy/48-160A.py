def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, = read_ints()
arr = read_ints()


def solve(arr: list) -> int:
    arr.sort(reverse=True)
    total_sum = sum(arr)
    left = 0
    for i in range(n):
        left += arr[i]
        right = total_sum - left
        if left > right:
            return i+1


print(solve(arr))

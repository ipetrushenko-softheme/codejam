def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]

import math

n, = read_ints()
arr = read_ints()


def solve(arr: list) -> int:
    ans = 0
    for i, el in enumerate(arr):
        if el < 0:
            ans += (-1 - el)
            arr[i] = -1
        elif el > 0:
            ans += (el - 1)
            arr[i] = 1
    k = sum(1 for el in arr if el == 0)
    if k > 0:
        return ans + k
    if k == 0:
        s = 1
        for el in arr:
            s *= el
        if s == 1:
            return ans
        return ans + 2


print(solve(arr))

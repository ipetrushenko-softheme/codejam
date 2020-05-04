def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


arr = read_ints()


def sq(a: int) -> int:
    return a*a


def sorted_squares(arr: list) -> list:
    n = len(arr)
    m = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            m = i
            break
    i = m - 1
    j = m
    c = [0]*n
    k = 0
    while i > -1 and j < n:
        if sq(arr[i]) < sq(arr[j]):
            c[k] = sq(arr[i])
            i = i - 1
        elif sq(arr[i]) >= sq(arr[j]):
            c[k] = sq(arr[j])
            j = j + 1
        k = k + 1

    while i > -1:
        c[k] = sq(arr[i])
        i = i - 1
        k = k + 1

    while j < n:
        c[k] = sq(arr[j])
        j = j + 1
        k = k + 1

    return c


# O(n*logn)
def sorted_squares_slow(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] * arr[i]

    arr.sort()
    return arr


print(sorted_squares(arr))
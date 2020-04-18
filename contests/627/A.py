def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def is_possible(arr: list) -> bool:
    minim = min(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] - minim

    if all_zero(arr):
        return True

    return all(el % 2 == 0 for el in arr)


def all_zero(arr):
    return all(el == 0 for el in arr)


T, = read_ints()
for test in range(T):
    n, = read_ints()
    arr = read_ints()
    ok = is_possible(arr)
    if ok:
        print("YES")
    else:
        print("NO")
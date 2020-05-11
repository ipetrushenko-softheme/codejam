def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def solve(arr: list) -> tuple:
    i = 1
    j = len(arr) - 1
    alica = False
    curr_alica = arr[0]
    curr_bob = 0
    total = 1
    total_alica = curr_alica
    total_bob = 0
    while j >= i:
        if alica:
            while curr_alica <= curr_bob and j >= i:
                curr_alica += arr[i]
                total_alica += arr[i]
                i += 1
            curr_bob = 0
        else:
            while curr_bob <= curr_alica and j >= i:
                curr_bob += arr[j]
                total_bob += arr[j]
                j -= 1
            curr_alica = 0
        total += 1
        alica = not alica

    return total, total_alica, total_bob


T = int(input())

for test in range(T):
    n, = read_ints()
    arr = read_ints()
    a, b, c = solve(arr)
    print(f"{a} {b} {c}")

def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, = read_ints()
arr = read_ints()


def solve(arr) -> str:
    for el in arr:
        if el == 1:
            return "HARD"
    return "EASY"


ans = solve(arr)
print(ans)

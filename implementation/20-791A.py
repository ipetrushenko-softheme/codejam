def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


a, b = read_ints()


def solve(a, b) -> int:
    years = 0
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    return years


print(solve(a, b))

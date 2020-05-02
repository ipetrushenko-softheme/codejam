def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, = read_ints()
s = input().strip()


def solve(s: str) -> str:
    if len(set(s.lower())) >= 26:
        return "YES"
    return "NO"


print(solve(s))

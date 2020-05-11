def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, k = read_ints()
s = input()
chars = read_tokens()


def solve_slow(s: str, chars: list) -> int:
    cnt = 0
    n = len(s)
    unique_chars = set(chars)
    i = 0
    while i < n:
        if s[i] not in unique_chars:
            i = i + 1
            continue

        for j in range(i, n):
            if s[j] not in unique_chars:
                diff = j-i
                cnt += (diff-1)*diff//2
                i = j
                break
            cnt += 1
        i = i + 1
    return cnt


def solve(s, chars):
    cnt = 0
    n = len(s)
    unique = set(chars)
    i = 0
    while i < n:
        j = i
        while j < n and s[j] in unique:
            j += 1
        diff = j - i
        cnt += diff * (diff + 1) // 2
        if i != j:
            i = j
        else:
            i += 1
    return cnt


print(solve(s, chars))

# https://codeforces.com/problemset/problem/1221/C


def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def good_enough(c, m, x, command) -> bool:
    _c = c - command
    _m = m - command
    if _c < 0 or _m < 0:
        return False

    _x = x - command
    if _x >= 0:
        return True

    if _c >= command or _m >= command or x >= command:
        return True

    return _c + _m + x >= command


def find_most(c, m, x) -> int:
    if c > m:
        x += c - m
        c = m
    else:
        x += m-c
        m = c

    bad = -1
    good = min(c, m) + 1

    while good - bad > 1:
        command = (good + bad) // 2
        if good_enough(c, m, x, command):
            bad = command
        else:
            good = command
    return bad


T, = read_ints()

for t in range(T):
    c, m, x = read_ints()
    print(find_most(c, m, x))

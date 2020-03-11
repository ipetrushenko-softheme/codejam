# https://codeforces.com/problemset/problem/1131/C


def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, = read_ints()
a = read_ints()

def good(a, sz):
    n = len(a)
    for i in range(n-1):
        if abs(a[i+1] - a[i]) > sz:
            return False

    if abs(a[0] - a[n-1]) > sz:
        return False
    return True

# 2 1 1 3 2
# 1 1 3 2 2
def min_diff(a: list):
    bad = -1
    good = max(a) + 1

    while bad - good > 1:
        sz = (good + bad) // 2
        if good(a, sz):
            good = sz
        else:
            bad = sz

    return good

# 2 1 1 3 2

# 1 1 2 2 3
# 1 1 2 3 2
# 1 1 3 2 2
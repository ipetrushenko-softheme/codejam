import itertools


def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def is_palindrome(a):
    n = len(a)
    for i in range(n//2):
        if a[i] != a[n-i-1]:
            return False
    return True


def recur_subset(s: list, ans:list, l=None) -> bool:
    if ans:
        return True
    if l is None:
        l = len(s)
    if l > 2:
        for x in itertools.combinations(s, l):
            if is_palindrome(list(x)):
                ans.append(list(x))
                return True
        a = recur_subset(s, ans, l-1)
        if a:
            return True


T, = read_ints()
for test in range(T):
    n, = read_ints()
    arr = read_ints()
    ok = recur_subset(arr, [])
    if ok:
        print("YES")
    else:
        print("NO")

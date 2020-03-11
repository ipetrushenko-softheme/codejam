# https://codeforces.com/problemset/problem/230/B
# preprocessing + binsearch 


def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


T, = read_ints()
numbers = read_ints()

# 10
# 10 9 8 7 6 5 4 3 2 1
# NO
# YES
# NO
# NO
# NO  6
# NO  5
# YES 4
# NO 3
# NO 2
# NO 1


import math
def f(n):
    unique = set([1, n])
    div = 2
    count = 0
    n = math.ceil(math.sqrt(n)) +1
    while n != 1 and n >= div:
        if n % div == 0:
            n = n // div
            unique.add(div)
            if len(unique) > 3:
                print("NO")
                return
            elif count > 1:
                print("NO")
                return
            count = count + 1
        if div == 2:
            div = div + 1
        else:
            div = div + 2

    count = len(unique)
    if n % 2 == 0 and n not in unique:
        count = count + 1
    print("YES" if count == 3 else "NO")


for num in numbers:
    f(num)

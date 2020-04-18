def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def f(n, a, b):
    substr = ''
    for i in range(b):
        substr += chr(97 + i)
    substr = substr * a
    while len(substr) < n:
        substr += substr
    return substr[:n]


T, = read_ints()
for test in range(T):
    n, a, b = read_ints()
    string = f(n, a, b)
    print(string)
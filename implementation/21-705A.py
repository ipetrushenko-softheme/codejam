def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, = read_ints()


def solve(n) -> str:
    ans = ''
    l = 'I love'
    h = 'I hate'
    hate = True
    while n != 0:
        if hate:
            ans = ans + h
        else:
            ans = ans + l

        hate = not hate
        n -= 1
        if n != 0:
            ans = ans + ' that '
    return ans + ' it'


print(solve(n))

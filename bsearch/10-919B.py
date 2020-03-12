def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


k, = read_ints()


def find_kth(n: int) -> int:
    el = 10
    while n:
        el += 9
        if sum(el) == 10:
            n -= 1
    return el


def sum(n: int) -> bool:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


print(find_kth(k))

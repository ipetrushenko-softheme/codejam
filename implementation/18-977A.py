def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, k = read_ints()

def solve(n, k):
    while k != 0:
        last_digit = n % 10
        if last_digit != 0:
            n -= 1
        if last_digit == 0:
            n //= 10

        k -= 1
    return n


print(solve(n, k))

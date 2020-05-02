from math import sqrt
n = int(input())


def is_prime(n: int) -> bool:
    sq = int(sqrt(n)) + 1
    for i in range(2, sq):
        if n % i == 0:
            return False

    return True


def solve(n: int) -> int:
    for m in range(1, 1001):
        ans = n*m + 1
        if not is_prime(ans):
            return m

print(solve(n))

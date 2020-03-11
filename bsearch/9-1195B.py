def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, k = read_ints()


def good_enough(n, k, m):
    cur_sum = arith_sum(m)
    return cur_sum - can_eat(n, m) >= k


def number_of_candies(n: int, k: int) -> int:
    bad = 0
    good = n + 1
    while good - bad > 1:
        m = (good + bad) // 2
        if good_enough(n,k, m):
            good = m
        else:
            bad = m

    return arith_sum(good) - k
    # for i in range(1, n+1):
    #     cur_sum = arith_sum(i)
    #     if cur_sum - can_eat(n, i) == k:
    #         return cur_sum - k


def can_eat(n, i):
    return n - i


def arith_sum(n: int) -> int:
    return (n + n*n) // 2


print(number_of_candies(n, k))

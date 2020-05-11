def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


T = int(input())

# y in S - x*n
# x*n + y = S ???
# S - x*n = сколько еще мне не хватает? 5 b 4


# def solve(a: int, b: int, n: int, S: int):
#     if b >= S:
#         return True
#
#     if a * n == S:
#         return True
#
#     if n + b == S or a * n + b == S:
#         return True
#
#     if n > S > b:
#         return False
#
#     for x in range(a + 1):
#         not_enough = S - x * n
#         if not_enough < 0:
#             return False
#         # if 0 <= not_enough <= b:
#         #    return True
#     return False


def solve(a: int, b: int, n: int, S: int) -> bool:
    if S % n > b:
        return False

    return a*n + b >= S


for test in range(T):
    a, b, n, S = read_ints()
    ok = solve(a, b, n, S)
    if ok:
        print("YES")
    else:
        print("NO")

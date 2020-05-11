T = int(input())


def find_max_ok(n: int) -> int:
    first = n
    total_digist = 1
    while first > 9:
        first = first // 10
        total_digist += 1

    return first * 10**(total_digist-1)


def solve(n: int) -> list:
    ans = []

    while n != 0:
        m = find_max_ok(n)
        ans.append(m)
        n -= m

    return ans


for test in range(T):
    n = int(input())
    arr = solve(n)
    print(len(arr))
    for el in arr:
        print(el, end=" ")
    print()

n = int(input())


def find_dev(a: int) -> set:
    ans = set()
    for i in range(2, a+1):
        while a != 1 and a % i == 0:
            a = a / i
            ans.add(i)
    return ans


def is_common_devisor(a: int, b: int) -> bool:
    s1 = find_dev(a)
    s2 = find_dev(b)
    return len(s1.intersection(s2)) > 0

def solve(n: int):
    for i in range(n-1, 0, -1):
        for j in range(n, 0, -1):
            if i < j and i + j == n and not is_common_devisor(i, j):
                return i, j


ans = solve(n)
print(f"{ans[0]} {ans[1]}")

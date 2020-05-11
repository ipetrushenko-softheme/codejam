def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def solve(n: int, k: int) -> list:
    ans = []
    if n < k:
        return ans

    if n % 2 != 0 and k % 2 == 0:
        return ans

    if n % k == 0:
        return [n // k] * k

    if n == k:
        return [1] * k

    if n % 2 == 0 and k % 2 != 0:
        if n < 2*k:
            return []
        for i in range(k-1):
            ans.append(2)
        ans.append(n - 2*(k-1))
        return ans

    if (n % 2 == 0 and k % 2 == 0) or (n % 2 != 0 and k % 2 != 0):
        for i in range(k-1):
            ans.append(1)
        ans.append(n - (k - 1))
        return ans

    return []


T = int(input())

for test in range(T):
    n, k = read_ints()
    arr = solve(n, k)
    if len(arr) == 0:
        print("NO")
        continue
    print("YES")
    for el in arr:
        print(el, end=" ")
    print()

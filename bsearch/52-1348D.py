def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


T, = read_ints()


def enough(days: int, number_of_vir: int) -> bool:
    # return  number_of_vir <= 2**days - 1
    return days + 1 <= number_of_vir <= 2**(days+1) - 1


def bs(n: int):
    bad = 0
    good = n
    while good - bad > 1:
        m = (good + bad) // 2
        if enough(m, n):
            good = m
        else:
            bad = m
    return good


for t in range(T):
    n = int(input())
    ans = bs(n)
    print(ans)
    res = []
    i = 1
    k = 1
    while n >= 2**k-1:
        res.append(i)
        i = i * 2
        k = k + 1
        ans -= 1
    res.append(n - (2**(k-1) -1))
    for i in range(len(res)-1):
        print(res[i+1]-res[i], end=" ")
    print()

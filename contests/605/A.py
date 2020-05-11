def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


T = int(input())


def solve(a: int, b: int, c: int) -> int:
    curr_min = float('inf')
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                first =  abs(a+i - (b+j))
                second = abs(a+i - (c+k))
                third =  abs(b+j - (c+k))
                total = first + second + third
                if curr_min > total:
                    curr_min = total
    return curr_min


for test in range(T):
    a, b, c = read_ints()
    min_diff = solve(a, b, c)
    print(min_diff)
# https://codeforces.com/problemset/problem/978/C


def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n, _ = read_ints()
flats_in = read_ints()
for i in range(1, n):
    flats_in[i] += flats_in[i-1]
letters = read_ints()


def find_f_k(flats_in: list, letter: int):
    bad = -1
    good = len(flats_in)

    while good - bad > 1:
        m = (good + bad) // 2
        if flats_in[m] >= letter:
            good = m
        else:
            bad = m

    prev_max = 0
    if good != 0:
        prev_max = flats_in[good-1]

    return good, abs(prev_max - letter)


for letter in letters:
    i, j = find_f_k(flats_in, letter)
    print(f"{i+1} {j}")


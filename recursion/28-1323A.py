def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def process_subset(arr, sofar):
    sum_so_far = 0
    for idx, el in enumerate(sofar):
        if el == 1:
            sum_so_far += arr[idx]

    return sum_so_far


def compute_subset(n, arr, sofar, ans):
    if not ans:  # without this check it doesnt work
        if not n:
            curr_sum = process_subset(arr, sofar)
            if curr_sum != 0 and curr_sum % 2 == 0:
                ans.append(sofar)
        else:
            compute_subset(n-1, arr,  sofar + [0], ans)
            compute_subset(n-1, arr, sofar + [1], ans)


T, = read_ints()
for test in range(T):
    n, = read_ints()
    arr = read_ints()
    ans = []
    compute_subset(len(arr), arr, [], ans)
    if not ans:
        print(-1)
    else:
        first = ans[0]
        c = sum(1 for el in first if el == 1)
        print(c)
        for idx, el in enumerate(first):
            if el == 1:
                print(f"{idx+1} ", end='')
        print()

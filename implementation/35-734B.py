def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def compute(arr):
    curr_sum = 0
    count_of_256 = min(arr[0], arr[2], arr[3])
    for idx, el in enumerate(arr):
        if idx != 1:
            arr[idx] -= count_of_256
    curr_sum += 256 * count_of_256

    count_of_32 = min(arr[0], arr[1])
    curr_sum += 32 * count_of_32
    return curr_sum


arr = read_ints()
ans = compute(arr)
print(ans)

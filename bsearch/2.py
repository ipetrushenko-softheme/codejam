def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


# def compute_min_distance(arr: list):
#     n = len(arr)
#     min_dist = 2
#     for i in range(n):
#         for j in range(i+min_dist+1, n, min_dist):
#             diff = j - i + 1
#             print(f"{i} {j} diff = {diff} min_dist = {min_dist}")
#             if diff >= min_dist and good_enough(arr, i, j):
#                 min_dist = diff
#     return min_dist

# 9
# 2 2 1 1 1 2 2 2 2
# 0 3 diff = 4 min_dist = 2
# 0 7 diff = 8 min_dist = 4
# 1 6 diff = 6 min_dist = 4
# 2 7 diff = 6 min_dist = 4

def compute_min_distance(arr: list):
    n = len(arr)
    m = n // 2
    min_dist = 2
    for i in range(m):
        j = i+min_dist+1
        while j < n:
            diff = j - i + 1
            # print(f"{i} {j} diff = {diff} min_dist = {min_dist}")
            if good_enough(arr, i, j):
                min_dist = diff
            j = j + min_dist
    return min_dist


def good_enough(a, i, j):
    mid = (j - i + 1) // 2
    curr_el = a[i]
    for k in range(mid):
        if (a[i] == a[j - k]) or (a[i] != curr_el):
            return False
        i = i + 1
    return True



# n, = read_ints()
#a = read_ints()
#print(compute_min_distance(a))

# stress
# n = 100      0.0007
# n = 1000     0.05
# n = 10000    3.95

import random
import time
n = 10000
a = [random.randrange(1, 3) for _ in range(n)]
st = time.time()
print(compute_min_distance(a))
print(time.time() - st)
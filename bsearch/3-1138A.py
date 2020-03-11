# https://codeforces.com/problemset/problem/1138/A


def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


# def good_enough(a, i, j):
#     mid = (j - i + 1) // 2
#     curr_el = a[i]
#     for k in range(mid):
#         b = a[i]
#         if (b == a[j - k]) or (b != curr_el):
#             return False
#         i = i + 1
#     return True

# def compute_min_distance(arr: list):
#     i = 0
#     n = len(arr)
#     mid = n // 2
#     min_dist = 2
#     while i < mid:
#         j = i + min_dist + 1
#         k = 2
#         prev = min_dist
#         cur = min_dist
#         while j < n:
#             diff = j - i + 1
#             print(f"{i} {j} diff {diff} min_dist {min_dist}")
#             if good_enough(arr, i, j):
#                 min_dist = diff
#                 cur = min_dist
#                 break
#             j = j + k
#             if j > n:
#                 j = n
#             k = k * 2
#
#         if prev != cur:
#             i = i + min_dist//2
#         else:
#             i = i + 1
#     return min_dist


def compute_min_distance(a):
    n = len(a)
    count_equal = 1
    length = []
    for i in range(n-1):
        if a[i] != a[i+1]:
            length.append(count_equal)
            count_equal = 0
        count_equal += 1

    length.append(count_equal)
    m = len(length)
    ans = 0
    for i in range(m - 1):
        ans = max(ans, min(length[i], length[i+1]))
    return ans * 2


_, = read_ints()
a = read_ints()
print(compute_min_distance(a))

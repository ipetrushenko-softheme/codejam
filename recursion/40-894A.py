s = input().strip()


# doesn't work on IAQVAQZLQBQVQFTQQQADAQJA
# def solve(s: str) -> int:
#     n = len(s)
#     pw = 2**n
#     count = 0
#     for mask in range(pw):
#         subset = []
#         for i in range(n):
#             if mask & (1 << i):
#                 subset.append(s[i])
#             if len(subset) == 4:
#                 break
#         if len(subset) == 3 and subset == ['Q', 'A', 'Q']:
#             count += 1
#
#     return count


def solve(s: str) -> int:
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == 'Q':
            for j in range(i+1, n):
                if s[j] == 'A':
                    for k in range(j+1, n):
                        if s[k] == 'Q':
                            count += 1
    return count


print(solve(s))

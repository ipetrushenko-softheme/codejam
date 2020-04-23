def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


def compute(arr):
    count = 0
    for our in arr:
        for their in arr:
            if our != their:
                if our[0] == their[1]:
                    count += 1
    return count


T, = read_ints()
forma = []
for _ in range(T):
    a, b = read_ints()
    forma.append((a, b))


ans = compute(forma)
print(ans)
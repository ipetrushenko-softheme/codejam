def read_tokens():
    return input().strip().split(' ')


def read_ints():
    return [int(s) for s in read_tokens()]


n = int(input())
arr = read_ints()
graph = [[] for _ in range(n)]
visited = [0] * n
parent = [-1] * n


def add_edge(u, v):
    global graph
    graph[u].append(v)


for u in range(n):
    v = arr[u]
    v = v - 1
    add_edge(u, v)

end = -1
start = -1


def dfs(u, depth):
    global visited
    global end
    global start
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 0:
            parent[u] = v
            if dfs(v, depth + 1):
                return True
        elif visited[v] == 1 and depth == 3:
            end = v
            start = u
            return True
    visited[u] = 2
    return False


def solve():
    global visited
    global end
    global start
    cycle = False
    for i in range(n):
        for j in range(n):
            # without this loop doesnt work!!!
            visited[j] = 0
        if visited[i] == 0 and dfs(i, 1):
            cycle = True
            break

    if start == -1 and not cycle:
        print("NO")
    else:
        ans = []
        ans.append(start)
        while end != start:
            ans.append(end)
            end = parent[end]
        ans.append(start)
        ans.reverse()
        if len(set(ans)) == 3:
            print("YES")
        else:
            print("NO")

solve()

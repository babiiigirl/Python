def dfs(u, v, ke, removed, visited):
    if u == v: return True
    visited[u] = True
    for x in ke[u]:
        if not visited[x] and x != removed:
            if dfs(x, v, ke, removed, visited): return True 
    return False

t = int(input())
for _ in range(t):
    n, m, u, v = map(int, input().split())
    ke = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        ke[a].append(b)
    cnt = 0
    for x in range(1, n + 1):
        if x == u or x == v:
            continue
        visited = [False] * (n + 1)
        if not dfs(u, v, ke, x, visited): cnt +=1
    print(cnt)   
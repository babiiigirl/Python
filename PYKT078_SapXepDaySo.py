t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    id = a.index(max(a))
    a.insert(id, m)
    for i in a:
        if i < 0: print(i, end=' ')
    for i in a:
        if i >= 0: print(i, end=' ')
    print()
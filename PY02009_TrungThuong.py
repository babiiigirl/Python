t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    for _ in range(n):
        x = int(input())
        if x in d: d[x] += 1
        else: d[x] = 1
    a = list(d.items())
    a.sort(key = lambda x : (-x[1], x[0]))
    print(a[0][0])
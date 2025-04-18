t = int(input())
for _ in range(t):
    n = int(input())
    a = set(list(map(int, input().split())))
    l = max(a)
    r = min(a)
    print(l - r + 1 - len(a))
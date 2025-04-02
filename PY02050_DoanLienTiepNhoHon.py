t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [-1] * n
    c = []
    for i in range(n):
        while (len(c) > 0 and a[c[-1]] <= a[i]): c.pop()
        if (len(c) > 0): b[i] = c[-1]
        c.append(i)
    for i in range(n):
        print(i - b[i], end = ' ')
    print()
t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            s += (1/i)
    else:
        for i in range(1, n + 1, 2):
            s += (1/i)
    print('%.6f' % s)
        
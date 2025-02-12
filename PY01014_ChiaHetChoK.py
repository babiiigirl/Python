a, k, n = map(int, input().split())
if (a < n):
    m = ((a // k) + 1) * k
    if (m > n): print(-1)
    else:   
        for i in range(m, n +1, k):
            print(i - a, end = ' ')
else:
    print('-1')
t = int(input())
for _ in range(t):
    cnt = 0
    n, x, m = map(float, input().split())
    while n < m:
        n *= (1 + x/100)
        cnt += 1
    print(cnt)
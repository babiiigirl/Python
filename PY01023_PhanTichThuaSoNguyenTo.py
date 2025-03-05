from math import *
t = int(input())
for _ in range (t):
    n = int(input())
    res = '1'
    for i in range(2, isqrt(n) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt > 0:
            res += ' * ' + str(i) + '^' + str(cnt)
    if n > 1:
        res += ' * ' + str(n) + '^1'
    print(res)
        
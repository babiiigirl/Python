from math import *

n, k = map(int, input().split())
cnt = 0
res = ''
for i in range(10 ** (k - 1), 10 ** k):
    if gcd(n, i) == 1:
        res += str(i) + ' '
        cnt += 1
    if cnt == 10:
        res += '\n'
        cnt = 0
print(res)
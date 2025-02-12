def solve(a, b):
    ucln = gcd(a, b)
    tong = 0
    while ucln > 0:
        tong = tong + ucln % 10
        ucln = ucln//10
    if isPrime(tong): return True
    else: return False

from math import *
def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if solve(a, b): print('YES')
    else: print('NO')
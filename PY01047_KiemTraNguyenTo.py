from math import *
def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return (n > 1)

t = int(input())
for _ in range(t):
    s = input()
    n = ''
    for i in range(len(s) - 4, len(s)):
        n += s[i]
    if isPrime(int(n)): print('YES')
    else: print('NO')
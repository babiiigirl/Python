from math import *
def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return (n > 1)

t = int(input())
for _ in range(t):
    s = input()
    check = False
    if isPrime(len(s)):
        cnt = 0
        for i in s:
            if i == '2' or i == '3' or i == '5' or i == '7': cnt += 1
        if len(s) - cnt < cnt: check = True
    if check: print('YES')
    else: print('NO')
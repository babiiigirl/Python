from math import *
def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        for i in range(1, n + 1):
            if gcd(i, n) == 1:
                cnt += 1
        if isPrime(cnt): print('YES')
        else: print('NO')
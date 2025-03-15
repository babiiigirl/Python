from math import *

prime = [True] * (10 ** 6 + 1)
def sieve():
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(10 ** 6) + 1):
        if prime[i]:
            for j in range(i * i, 10 ** 6 + 1, i):
                prime[j] = False
                
if __name__ == '__main__':  
    sieve()      
    n, x = map(int, input().split())
    primes = [0]
    for i in range(2, 10 ** 6 + 1):
        if prime[i]:
            primes.append(i)
    for i in range(n + 1):
        print(x + primes[i], end = ' ')
        x = x + primes[i]
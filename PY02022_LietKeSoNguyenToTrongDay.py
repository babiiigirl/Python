from math import *
def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return (n > 1)

def countFrequency(a):
    d = {}
    for i in a:
        if i in d: d[i] += 1
        else: d[i] = 1
    arr = list(d.items())
    # arr.sort(key = lambda x : (x[1]))
    return arr

n = int(input())
a = list(map(int, input().split()))
arr = countFrequency(a)
for i in range (len(arr)):
        if isPrime(arr[i][0]): print(arr[i][0], arr[i][1])
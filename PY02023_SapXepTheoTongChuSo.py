def sumDigit(n):
    res = 0
    while n != 0:
        res += n % 10
        n//= 10
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.sort(key = sumDigit)
    for i in a: 
        print(i, end = ' ')
    print()
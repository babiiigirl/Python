def plusDigit(n):
    res = 1
    while n != 0:
        res *= n % 10
        n//= 10
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.sort(key = plusDigit)
    for i in a: 
        print(i, end = ' ')
    print()
def fibo(n):
    if n == 1 or n == 2:
        return 1
    fn1, fn2 = 1, 1
    for i in range(2, n):
        fn = fn1 + fn2
        fn2, fn1 = fn1, fn
    return fn

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(fibo(i), end = ' ')
    print()
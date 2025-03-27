while True:
    n = int(input())
    if n == 0: break
    a = []
    a.append(n)
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n *3 + 1
        a.append(n)
    print(len(a)) 
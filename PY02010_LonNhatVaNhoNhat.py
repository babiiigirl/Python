while True:
    n = int(input())
    if n == 0: break
    a = []
    for i in range(n):
        a.append(int(input()))
    if (min(a) == max(a)): print("BANG NHAU")
    else: print(min(a), max(a))
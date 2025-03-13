def check(n):
    if (len(n) < 3): return False
    k = 0
    ok = False
    for i in range(1, len(n)):
        if (n[i] > n[i - 1]):
            continue
        elif (n[i] < n[i - 1]):
            ok = True
            k = i
            break
        else: return False
    if not ok: return False
    for i in range (k - 1, len(n) - 1):
        if (n[i] <= n[i + 1]):
            return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    if check(n): print("YES") 
    else: print("NO")
    
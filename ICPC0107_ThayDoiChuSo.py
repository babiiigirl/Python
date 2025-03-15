t = int(input())
for _ in range(t):
    p, q = map(str, input().split())
    s = input().split() 
    if len(s) > 1: 
        x1, x2 = s[0], s[1] 
    else: 
        x1 = s[0] 
        x2 = input().strip()
    nho = min(p, q)
    lon = max(p, q)
    min = int(x1.replace(lon, nho)) + int(x2.replace(lon, nho))
    max = int(x1.replace(nho, lon)) + int(x2.replace(nho, lon))
    print(min, max)
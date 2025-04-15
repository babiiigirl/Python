n = int(input())
a = []
for _ in range(n):
    a.append(input())
s = a[0]
check = True
minn = 10 ** 9
for i in range(len(s)):
    cnt = 0
    for j in range(n):
        x = a[j]
        for k in range(len(s)):
            if x == s: 
                cnt += k
                break
            x = x[1:] + x[0]
        if x != s: check = False
    minn = min(minn, cnt)
    s = s[1:] + s[0]
if(check): print(minn)
else: print(-1) 
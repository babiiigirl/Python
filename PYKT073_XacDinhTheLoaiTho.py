n = int(input())
a = []
theTho = []
cnt = 0
for i in range(n):
    s = input().split()
    if len(a) == 0 and len(s) == 6: theTho.append(1)
    a.append(s)
    if len(a) > 1 and len(s) == 6 and len(a[-2]) == 7: theTho.append(1)
    if len(s) == 7: cnt += 1
    if cnt == 4: 
        theTho.append(2)
        cnt = 0

print(len(theTho))
for i in theTho: print(i)
a = list(input().split())
for i in range(len(a)):
    if i != 1 and i != 3:
        a[i] = int(a[i])
if a[0] + a[2] == a[4]:
    print('YES')
else: print('NO')
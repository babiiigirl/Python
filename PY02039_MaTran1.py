n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
k = int(input())
tong_tren = tong_duoi = 0
for i in range(n):
    for j in range(n):
        if i < j: tong_tren += a[i][j]
        elif i > j: tong_duoi += a[i][j]
if abs(tong_tren - tong_duoi) <= k:
    print('YES')
else: print('NO')
print(abs(tong_tren - tong_duoi))
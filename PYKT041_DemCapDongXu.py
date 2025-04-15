n = int(input())
a = list()
for i in range(n):
    a.append(input())
cnt = 0
for i in range(n):
    coin = 0
    for j in a[i]:
        if j == 'C': coin += 1
    cnt += (coin - 1)*coin//2
for j in range(n):
    coin = 0
    for i in range(n):
        if a[i][j] == 'C': coin += 1
    cnt += (coin - 1)*coin//2
print(cnt)
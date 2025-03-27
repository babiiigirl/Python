t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d: d[i] += 1
        else: d[i] = 1
    arr = list(d.items())
    arr.sort(key = lambda x : (-x[1], x[0]))
    if arr[0][1] > (n/2):
        print(arr[0][0])
    else: print('NO')
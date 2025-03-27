def solve(arr):
    return [
        abs(arr[0] - arr[1]),
        abs(arr[1] - arr[2]),
        abs(arr[2] - arr[3]),
        abs(arr[3] - arr[0])
    ]
while True:
    a = list(map(int, input().split()))
    if a == [0] * 4: break
    cnt = 0
    while True:
        if a.count(a[0]) == len(a): break
        a = solve(a)
        cnt += 1
    print(cnt)
        
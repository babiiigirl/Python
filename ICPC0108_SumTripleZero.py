t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            cursum = a[i] + a[left] + a[right]
            if cursum == 0:
                cnt += 1
                left += 1
                right -= 1
            elif cursum < 0:
                left += 1
            else:
                right -= 1
    print(cnt)
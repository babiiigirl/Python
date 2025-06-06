t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if str(sum) == str(sum)[::-1] and sum > 10: print('YES')
    else: print('NO')
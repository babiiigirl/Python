t = int(input())
for _ in range(t):
    s = input()
    check = True
    for i in s:
        if i != '0' and i != '1' and i != '2':
            check = False
            print('NO')
            break
    if check: print('YES')
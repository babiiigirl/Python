t = int(input())
for _ in range(t):
    s = input()
    a = s[0:2]
    b = s[(len(s) - 2):(len(s))]
    if a == b:
        print('YES')
    else: print('NO')
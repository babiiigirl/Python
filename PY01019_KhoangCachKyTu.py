t = int(input())
for _ in range (t):
    s = input()
    t = s[::-1]
    check = True
    for i in range (1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(t[i]) - ord(t[i - 1])):
            check = False
    if check:
        print('YES')
    else:
        print('NO')
    
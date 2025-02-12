def giaiMa(s):
    t = ''
    for i in range(len(s) - 1):
        if i % 2 == 0:
            t = t + s[i] * int(s[i + 1])
    return t

t = int(input())
for _ in range(t):
    s = input()
    print(giaiMa(s))
def maHoa(s):
    t = ''
    cnt = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            t = t + str(cnt) + s[i]
            cnt = 1
    t += str(cnt) + s[-1]
    return t

t = int(input())
for _ in range(t):
    s = input()
    print(maHoa(s))
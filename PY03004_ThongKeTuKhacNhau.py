t = int(input())
d = {}
for _ in range(t):
    s = input().lower()
    t = ''
    for i in s:
        if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
            t += i
        else: t += ' '
    a = list(t.split())
    for i in a:
        if i in d: d[i] += 1
        else: d[i] = 1
arr = list(d.items())
arr.sort(key = lambda x: (-x[1], x[0]))
for x in arr:
    print(x[0], x[1])
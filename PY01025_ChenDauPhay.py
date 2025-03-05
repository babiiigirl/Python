n = input()
cnt = 0
res = ""
for i in range(-1, len(n) * -1 -1, -1):
    res += n[i]
    cnt += 1
    if cnt % 3 == 0:
        res += ','
res = res[::-1]
if res[0] == ',':
    res = res[1:]
print(res)
p = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
while True:
    str = input()
    k = int(str.split()[0])
    if k == 0:
        break
    s = str.split()[1]
    res = ""
    if k > 0:
        for char in s:
            if char in p:
                idx = p.index(char)
                i = (idx + k) % 28
                res += p[i]       
    print(res[::-1])
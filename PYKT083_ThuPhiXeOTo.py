t = int(input())
ngay_set = set()
a = []
for _ in range(t):
    s = input().split()
    a.append(s)
    ngay_set.add(s[4])
ngay = list(ngay_set)
ngay.sort(key=lambda x: (int(x[6:]), int(x[3:5]), int(x[:2])))
for i in ngay:
    print(i + ':', end=' ')
    sum = 0
    for j in a:
        if i == j[4] and j[3] == 'IN':
            if j[2] == '5': sum += 10000
            elif j[2] == '7': sum += 15000
            elif j[2] == '2': sum += 20000
            elif j[2] == '29': sum += 50000
            else: sum += 70000
    print(sum)
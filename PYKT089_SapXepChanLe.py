n = int(input())
a = list(map(int, input().split()))
evens = []
odds = []
type = []
for x in a:
    if x % 2 == 0:
        evens.append(x)
        type.append('even')
    else:
        odds.append(x)
        type.append('odd')
evens.sort()
odds.sort(reverse=True)
res = []
eid = 0
oid = 0
for t in type:
    if t == 'even':
        res.append(evens[eid])
        eid += 1
    else:
        res.append(odds[oid])
        oid += 1   
print(*res) 
n = int(input())
a = []
while True :
    x = [int(x) for x in input().split()]
    a += x
    if len(a) == n : break
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
evens.sort(reverse=True)
odds.sort()
res = []
for t in type:
    if t == 'even':
        res.append(evens[-1])
        evens.pop()
    else:
        res.append(odds[-1])
        odds.pop() 
print(*res) 
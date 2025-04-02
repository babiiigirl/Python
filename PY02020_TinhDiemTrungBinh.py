n = int(input())
a = list(map(float, input().split()))
min = min(a)
max = max(a)
for i in a:
    if i == max or i == min:
        a.remove(i)
print('%.2f' % (sum(a)/len(a)))

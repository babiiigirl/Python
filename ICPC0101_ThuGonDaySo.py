from inspect import stack

n = int(input())
a = list(map(int, input(). split()))
s = []
s.append(a[0])
for i in range (1, len(a)):
    if len(s) and (a[i] + s[-1]) % 2 == 0:
        s.pop()
    else:
        s.append(a[i])
print(len(s))
        
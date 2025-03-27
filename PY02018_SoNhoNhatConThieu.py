n = int(input())
a = list(map(int, input().split()))
a.sort()
check = False 
for i in range(n - 1):
    if a[i] + 1 < a[i + 1]: 
        print(a[i] + 1)
        check = True
        break
if check == False:
    print(a[n - 1] + 1)
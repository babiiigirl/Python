def check(n):
    sum = 0
    for i in range (len(n) - 1):
        if (abs(int(n[i]) - int(n[i + 1])) != 2):
            return False
        sum += int(n[i])
    sum += int(n[-1])
    if sum % 10 != 0:
        return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
        
    
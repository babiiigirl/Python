def check(n):
    s = set(n)
    if len(s) != 2:
        return False
    for i in range (len(n) - 2):
        if n[i] != n[i+2]:
            return False 
    return True    

t = int(input())
for _ in range(t):
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')
    
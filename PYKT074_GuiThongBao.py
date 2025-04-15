t = int(input())
for _ in range(t):
    s = input()
    if len(s) <= 100: 
        print(s)
    else:
        a = list(s.split())
        str = ''
        for i in a: 
            str += i + ' '
            if len(str) <= 100: print(i, end = ' ')
        print()
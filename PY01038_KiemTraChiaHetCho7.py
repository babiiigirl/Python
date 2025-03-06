t = int(input())

for _ in range(t):
    n = input()
    cnt = 0
    if (int(n) % 7 == 0):
        print(n)
    else:
        while (int(n) + int(n[::-1])) % 7 != 0 and cnt <= 1000:
            cnt += 1
            n = str(int(n) + int(n[::-1]))  
        if cnt < 1000: 
            n = str(int(n) + int(n[::-1]))
            print(n)
        else:
            print(-1)
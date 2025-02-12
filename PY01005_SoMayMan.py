def count(s):
    cnt = 0
    for i in range(len(s)):
        if (s[i] == '4' or s[i] == '7'): 
            cnt += 1
    return cnt

if __name__ == '__main__':
    s = input()
    if (count(s) == 4 or count(s) == 7): print('YES')
    else: print('NO')
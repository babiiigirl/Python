def luckyNumber(s):
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        if luckyNumber(n):
            print('YES')
        else:
            print('NO')
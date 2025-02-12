s = input()
hoa = 0
thuong = 0
for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        thuong += 1
    else: 
        hoa += 1
if hoa > thuong:
    print(s.upper())
else: 
    print(s.lower())
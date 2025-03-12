from math import *
def decimaltobase4(n):
    digits = []
    while n > 0:
        digits.append(str(n % 4))
        n //= 4
    s = digits[::-1]
    return ''.join(s)

t = int(input())
for _ in range(t):
    b = int(input())
    x = input()
    decimal_value = int(x, 2)
    res = ''
    if b == 2:
        print(format(decimal_value, 'b'))
    elif b == 8:
        print(format(decimal_value, 'o'))
    elif b == 4:
        print(decimaltobase4(decimal_value))
    else:
        print(format(decimal_value, 'X'))
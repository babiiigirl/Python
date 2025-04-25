def chuyen_co_so(n, b):
    if n == 0: return '0'
    chu_so = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ket_qua = ""
    while n > 0:
        du = n % b
        ket_qua = chu_so[du] + ket_qua
        n = int(n / b)
    return ket_qua

t = int(input())
for _ in range(t):
    n, b = map(int, input().split())
    print(chuyen_co_so(n, b))
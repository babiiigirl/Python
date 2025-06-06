listSTN = []
chan = ['0', '2', '4', '6', '8']
def soThuanNghich(chuoi_nua_dau): #chuoi_nua_dau: chuoi cua nua dau so thuan nghich
    listNguoc = list(chuoi_nua_dau)
    listNguoc.reverse()
    chuoi_nua_dao_nguoc = ''.join(listNguoc)
    stn = int(chuoi_nua_dau + chuoi_nua_dao_nguoc)
    global listSTN
    listSTN.append(stn)
    if len(chuoi_nua_dau) < 3:
        for i in chan:
            soThuanNghich(chuoi_nua_dau + i)

for i in chan[1:]:
    soThuanNghich(i)
listSTN.sort()
t = int(input())
for _ in range(t):
    n = int(input())
    for i in listSTN:
        if i < n: print(i, end=' ')
        else: break
    print()
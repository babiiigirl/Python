from datetime import datetime
class CaThi:
    def __init__(self, ma, maMon, tenMon, ngayThi, gioThi, nhomThi):
        self.ma = f'T{ma:03d}'
        self.maMon = maMon
        self.tenMon = tenMon
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.nhomThi = nhomThi
    
    def __str__(self):
        return f'{self.ma} {self.maMon} {self.tenMon} {self.ngayThi} {self.gioThi} {self.nhomThi}'
        
n, m = map(int, input().split())
dictMon = {}
for _ in range(n):
    maMon = input()
    tenMon = input()
    dictMon[maMon] = tenMon
listCaThi = []
for i in range(m):
    s = input().split()
    ma = i + 1
    maMon = s[0]
    tenMon = dictMon[maMon]
    ngayThi = s[1]
    gioThi = s[2]
    nhomThi = s[3]
    ca = CaThi(ma, maMon, tenMon, ngayThi, gioThi, nhomThi)
    listCaThi.append(ca)
listCaThi.sort(key = lambda x : (datetime.strptime(x.ngayThi, "%d/%m/%Y"), x.gioThi, x.maMon))
for ca in listCaThi:
    print(ca)
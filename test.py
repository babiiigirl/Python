class MonHoc:
    def __init__(self, maCa, maMon, ten, ngayThi, gioThi, nhom):
        self.maCa = 'T{:03d}'.format(maCa)
        self.maMon = maMon
        self.ten = ten
        self.ngayThi = ngayThi
        self.ngay = int(ngayThi[:2])
        self.thang = int(ngayThi[3:5:])
        self.nam = int(ngayThi[6:])
        self.gioThi = gioThi
        self.gio = int(gioThi[:2])
        self.phut = int(gioThi[3:])
        self.nhom = nhom
    def __str__(self):
        return self.maCa + " " + self.maMon + " " + self.ten + " " + self.ngayThi + " " + self.gioThi + " " + self.nhom

d = {}
n, m = map(int, input().split())
for _ in range(n):
    maMon = input()
    tenMon = input()
    d[maMon] = tenMon
a = []
for i in range(m):
    maMon, ngayThi, gioThi, nhom = input().split()
    a.append(MonHoc(i + 1, maMon, d[maMon], ngayThi, gioThi, nhom))
a.sort(key = lambda x : (x.nam, x.thang, x.ngay, x.gio, x.phut, x.maMon))
for i in a:
    print(i)
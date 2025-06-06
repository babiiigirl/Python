class NhanVien:
    def __init__(self, ma, ten, lyThuyet, thucHanh):
        self.ma = 'TS0' + str(ma) #WA thường xảy ra ở đây nếu self.ma = f'TS{ma:02d}'
        self.ten = ten
        while lyThuyet > 10.0:
            lyThuyet /= 10.0
        while thucHanh > 10.0:
            thucHanh /= 10.0
        self.trungBinh = (lyThuyet + thucHanh) / 2
    
    def xepLoai(self):
        if self.trungBinh< 5:
            return 'TRUOT'
        elif self.trungBinh < 8:
            return 'CAN NHAC'
        elif self.trungBinh < 9.5:
            return 'DAT'
        else:
            return 'XUAT SAC'
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.trungBinh:.2f} {self.xepLoai()}'

t= int(input())
listNhanVien = []
for i in range(t):
    nv = NhanVien(i + 1, input().strip(), float(input().strip()), float(input().strip()))
    listNhanVien.append(nv)
listNhanVien.sort(key=lambda x: x.trungBinh, reverse=True)
for nv in listNhanVien:
    print(nv)
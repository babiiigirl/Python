from decimal import Decimal, ROUND_HALF_UP

class HocSinh:
    def __init__(self, ma, ten, diem):
        self.ma = f'{ma:02d}'
        self.ten = ten
        self.diem = diem
    
    def diemTrungBinh(self):
        tb = (self.diem[0] *2 + self.diem[1] * 2 + sum(self.diem[2:]))/12
        return tb.quantize(Decimal('0.1'), ROUND_HALF_UP)
    
    def hocLuc(self):
        dtb = float(self.diemTrungBinh())
        if dtb >= 9.0:
            return "XUAT SAC"
        elif dtb >= 8.0:
            return "GIOI"
        elif dtb >= 7.0:
            return "KHA"
        elif dtb >= 5.0:
            return "TB"
        else:
            return "YEU"
    def __str__(self):
        return f"HS{self.ma} {self.ten} {self.diemTrungBinh():.1f} {self.hocLuc()}"

t = int(input())
listHocSinh = []
for i in range(t):
    ten = input().strip()
    diem = list(map(Decimal, input().split()))
    hs = HocSinh(i + 1, ten, diem)
    listHocSinh.append(hs)
listHocSinh.sort(key=lambda x: (-x.diemTrungBinh(), x.ma))
for hs in listHocSinh:
    print(hs)
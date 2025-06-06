from datetime import datetime


class NguoiChoi:
    def __init__(self, ma, ten, batDau, ketThuc):
        self.ma = ma
        self.ten = ten
        self.batDau = batDau
        self.ketThuc = ketThuc

        time_format = "%H:%M"
        tBatDau = datetime.strptime(batDau, time_format)
        tKetThuc = datetime.strptime(ketThuc, time_format)
        khoangThoiGian = (tKetThuc - tBatDau).total_seconds() 
        self.thoiGian = khoangThoiGian
        self.gio = int(khoangThoiGian // 3600)
        self.phut = int((khoangThoiGian % 3600) // 60)

    def __str__(self):
        return f'{self.ma}  {self.ten} {self.gio} gio {self.phut} phut'

t = int(input())
listNguoiChoi = []
for _ in range(t):
    ma = input().strip()
    ten = input().strip()
    batDau = input().strip()
    ketThuc = input().strip()
    nguoiChoi = NguoiChoi(ma, ten, batDau, ketThuc)
    listNguoiChoi.append(nguoiChoi)

listNguoiChoi.sort(key=lambda x: x.thoiGian, reverse=True)
for nguoiChoi in listNguoiChoi:
    print(nguoiChoi)
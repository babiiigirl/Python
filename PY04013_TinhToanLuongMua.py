from datetime import datetime


class TramDo:
    def __init__(self, ten, tongLuongMua, thoiGian):
        self.ten = ten
        self.tongLuongMua = tongLuongMua
        self.thoiGian = thoiGian
    
    def themLanDo(self, batDau, ketThuc, luongMua):
        time_format = "%H:%M"
        tBatDau = datetime.strptime(batDau, time_format)
        tKetThuc = datetime.strptime(ketThuc, time_format)
        thoiGian = (tKetThuc - tBatDau).total_seconds() / 60
        self.tongLuongMua += luongMua
        self.thoiGian += thoiGian
        
    def trungBinhLuongMua(self):
        if self.thoiGian == 0:
            return 0.0
        return self.tongLuongMua / self.thoiGian * 60
    def __str__(self, ma):
        return f'T{ma:02d} {self.ten} {self.trungBinhLuongMua():.2f}'
    
t = int(input())
dictTram = {}
listTram = []
for _ in range(t):
    ten = input().strip()
    batDau = input().strip()
    ketThuc = input().strip()
    luongMua = float(input().strip())
    
    if ten not in dictTram:
        tram = TramDo(ten, 0, 0)
        dictTram[ten] = tram
        listTram.append(tram)
    dictTram[ten].themLanDo(batDau, ketThuc, luongMua)
    
ma = 1
for tram in listTram:
        print(tram.__str__(ma))
        ma += 1
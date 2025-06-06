from datetime import datetime
class CuaRo:
    def __init__(self, ten, donVi, thoiDiemDenDich):
        self.ma = "".join([word[0] for word in donVi.split() + ten.split()])
        self.ten = ten
        self.donVi = donVi
        self.thoiDiemDenDich = thoiDiemDenDich
        
    def vanToc(self):
        time_format = "%H:%M"
        batDau = datetime.strptime("06:00", time_format)
        denDich = datetime.strptime(self.thoiDiemDenDich, time_format)
        thoiGian = (denDich - batDau).total_seconds() / 3600
        return round(120/thoiGian)
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.donVi} {self.vanToc()} Km/h'
    
t = int(input())
listCR = []
for _ in range(t):
    cr = CuaRo(input().strip(), input().strip(), "0" + input().strip())
    listCR.append(cr)
listCR.sort(key = lambda x : x.thoiDiemDenDich, reverse=False)
for cr in listCR:
    print(cr)    
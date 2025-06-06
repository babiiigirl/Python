class HoaDon:
    def __init__(self, ma, ten, soLuong, donGia, tienCK):
        self.ma = ma
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.tienCK = tienCK
        
        self.tongTien = donGia * soLuong - tienCK
        
    def __str__(self):
        return f'{self.ma} {self.ten} {self.soLuong} {self.donGia} {self.tienCK} {self.tongTien}'
    
t = int(input())
listHD = []
for i in range(t):
    hd = HoaDon(input().strip(), input().strip(), int(input()), int(input()), int(input()))
    listHD.append(hd)
listHD.sort(key = lambda x : -x.tongTien)
for hd in listHD:
    print(hd)
from datetime import datetime
class KhachHang:
    def __init__(self, ma, ten, soPhong, ngayNhan, ngayTra, dichVu):
        self.ma = f'KH{ma:02d}'
        self.ten = ten
        self.soPhong = soPhong
        self.ngayNhan = ngayNhan
        self.ngayTra = ngayTra
        self.dichVu = dichVu
        
    def soNgayO(self):
        date_format = "%d/%m/%Y"
        ngayNhan = datetime.strptime(self.ngayNhan, date_format)
        ngayTra = datetime.strptime(self.ngayTra, date_format)
        return (ngayTra - ngayNhan).days + 1
    
    def tongTien(self):
        tang = int(self.soPhong[0])
        donGia = 0
        if tang == 1:
            donGia = 25
        elif tang == 2:
            donGia = 34
        elif tang == 3:
            donGia = 50
        else:
            donGia = 80
        return self.soNgayO() * donGia + self.dichVu
    def __str__(self):
        return f'{self.ma} {self.ten} {self.soPhong} {self.soNgayO()} {self.tongTien()}'
    
t = int(input())
listKH = []
for i in range(t):
    kh = KhachHang(i + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input()))
    listKH.append(kh)
listKH.sort(key=lambda x: x.tongTien(), reverse=True)
for kh in listKH:
    print(kh)
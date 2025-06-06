class KhachHang:
    def __init__(self, ma, ten, chiSoCu, chiSoMoi):
        self.ma = f'{ma:02d}'
        self.ten = ten
        self.chiSoCu = chiSoCu
        self.chiSoMoi = chiSoMoi
        
    def tongTien(self):
        soNuoc = self.chiSoMoi - self.chiSoCu
        tienNuoc = 0
        phuPhi = 0
        if soNuoc <= 50:
            tienNuoc = soNuoc * 100
            phuPhi = 0.02
        elif soNuoc <= 100:
            tienNuoc = 50 * 100 + (soNuoc - 50) * 150
            phuPhi = 0.03
        else:
            tienNuoc = 50 * 100 + 50 * 150 + (soNuoc - 100) * 200 
            phuPhi = 0.05
        return tienNuoc * (1 + phuPhi)
    def __str__(self):
        return f'KH{self.ma} {self.ten} {self.tongTien():.0f}'
    
t = int(input())
listKhachHang = []
for i in range(t):
    ten = input().strip()
    chiSoCu = int(input().strip())
    chiSoMoi = int(input().strip())
    kh = KhachHang(i + 1, ten, chiSoCu, chiSoMoi)
    listKhachHang.append(kh)
listKhachHang.sort(key=lambda x: (-x.tongTien(), x.ma))
for kh in listKhachHang:
    print(kh)
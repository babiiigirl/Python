class GiaoVien:
    def __init__(self, ma, ten, maxt, diemTin, diemCM):
        self.ma = f'GV{ma:02d}'
        self.ten = ten
        self.mon = ""
        if maxt[0] == 'A':
            self.mon = "TOAN"
        elif maxt[0] == 'B':
            self.mon = "LY"
        else: self.mon = "HOA"
        
        uuTien = 0
        if maxt[1] == '1':
            uuTien = 2.0
        elif maxt[1] == '2':
            uuTien = 1.5
        elif maxt[1] == '3':
            uuTien = 1.0
        else:
            uuTien = 0.0
        
        self.tongDiem = diemTin * 2 + diemCM + uuTien
        
        self.xepLoai = ""
        if self.tongDiem >= 18:
            self.xepLoai = "TRUNG TUYEN"
        else: self.xepLoai = "LOAI"
        
    def __str__(self):
        return f"{self.ma} {self.ten} {self.mon} {self.tongDiem:.1f} {self.xepLoai}"
    
t = int(input())
listGv = []
for i in range(t):
    gv = GiaoVien(i + 1, input().strip(), input().strip(), float(input().strip()), float(input().strip()))
    listGv.append(gv)
listGv.sort(key=lambda x : -x.tongDiem)
for gv in listGv:
    print(gv) 
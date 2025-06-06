class SinhVien:
    def __init__(self, ma, ten, lop, diem, ghiChu):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem = diem
        self.ghiChu = ""
        
    def tinhDiem(self, diemDanh):
        diem = 10
        for i in diemDanh:
            if i == 'v': diem-= 2
            elif i == 'm': diem -= 1
        self.diem = max(0, diem)
        if self.diem == 0:
            self.ghiChu = "KDDK"
            
    def __str__(self):
        return f'{self.ma} {self.ten} {self.lop} {self.diem} {self.ghiChu}'
    
t = int(input())
listSinhVien = []
dictSinhVien = {}
for _  in range(t):
    ma = input().strip()
    ten = input().strip()
    lop = input().strip()
    if ma not in dictSinhVien:
        sv = SinhVien(ma, ten, lop, 10, "")
        listSinhVien.append(sv)
        dictSinhVien[ma] = sv
    
for _ in range(t):
    s = input().strip()
    ma = s.split()[0]
    diemDanh = s.split()[1]
    if ma in dictSinhVien:
        dictSinhVien[ma].tinhDiem(diemDanh)
for sv in listSinhVien:
    print(sv)
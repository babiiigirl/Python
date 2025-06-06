def chuan_hoa_ten(ten):
    return ' '.join(word.capitalize() for word in ten.strip().split())

def tinh_uu_tien(khu_vuc, dan_toc):
    uu_tien = 0
    if khu_vuc == '1':
        uu_tien += 1.5
    elif khu_vuc == '2':
        uu_tien += 1.0
    # khu_vuc 3 không cộng gì
    if dan_toc.lower() != 'kinh':
        uu_tien += 1.5
    return uu_tien

class ThiSinh:
    def __init__(self, ma, ten, diem, dan_toc, khu_vuc):
        self.ma = ma
        self.ten = chuan_hoa_ten(ten)
        self.diem = float(diem)
        self.dan_toc = dan_toc
        self.khu_vuc = khu_vuc
        self.tong = self.diem + tinh_uu_tien(khu_vuc, dan_toc)
        self.trang_thai = "Do" if self.tong >= 20.5 else "Truot"

    def __lt__(self, other):
        if self.tong != other.tong:
            return self.tong > other.tong
        return self.ma < other.ma

    def __str__(self):
        return f"{self.ma} {self.ten} {self.tong:.1f} {self.trang_thai}"

n = int(input())
ds = []
for i in range(1, n+1):
    ten = input().strip()
    diem = input().strip()
    dan_toc = input().strip()
    khu_vuc = input().strip()
    ma = f"TS{str(i).zfill(2)}"
    ds.append(ThiSinh(ma, ten, diem, dan_toc, khu_vuc))

ds.sort()
for ts in ds:
    print(ts)
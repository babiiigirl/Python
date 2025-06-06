from datetime import datetime
class Phim:
    def __init__(self, ma, theLoai, ngayKC, ten, soTap):
        self.ma = f'P{ma:03d}'
        self.theLoai = theLoai
        self.ngayKC = ngayKC
        self.ten = ten
        self.soTap = soTap
        
    def __str__(self):
        return f'{self.ma} {self.theLoai} {self.ngayKC} {self.ten} {self.soTap}'
        
n, m = map(int, input().split())
dictTheLoai = {}
listPhim = []
for i in range(n):
    theLoai = input().strip()
    dictTheLoai[f'TL{(i+1):03d}'] = theLoai
for i in range(m):
    ma = i + 1
    theLoai = dictTheLoai[input().strip()]
    ngayKC = input().strip()
    ten = input().strip()
    soTap = int(input())
    phim = Phim(ma, theLoai, ngayKC, ten, soTap)
    listPhim.append(phim)
listPhim.sort(key= lambda x : (datetime.strptime(x.ngayKC, "%d/%m/%Y"), x.ten, -x.soTap))
for phim in listPhim:
    print(phim)
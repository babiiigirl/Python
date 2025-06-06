from math import gcd


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu = int(self.tu / ucln)
        self.mau = int(self.mau / ucln)
    def __str__(self):
        return f'{self.tu}/{self.mau}'
        
tu, mau = map(int, input().split())
p = PhanSo(tu, mau) 
p.rut_gon()
print(p)
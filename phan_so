from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        
    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu = int(self.tu / ucln)
        self.mau = int(self.mau / ucln)
    
    def add(self, other):
        a = self.tu * other.mau + other.tu * self.mau
        b = self.mau * other.mau
        self.tu = a
        self.mau = b
    
    def __str__(self):
        return f'{self.tu}/{self.mau}'

s = input().split()
p = PhanSo(int(s[0]), int(s[1]))
q = PhanSo(int(s[2]), int(s[3]))
p.add(q)
p.rut_gon()
print(p)
class ThiSinh:
    def __init__(self, ho_ten, ngay_sinh, diem1, diem2, diem3):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.diem1 = float(diem1)
        self.diem2 = float(diem2)
        self.diem3 = float(diem3)

    def tinh_tong_diem(self):
        return self.diem1 + self.diem2 + self.diem3

    def __str__(self):
        tong_diem = self.tinh_tong_diem()
        return f"{self.ho_ten} {self.ngay_sinh} {tong_diem:.1f}"

def main():
    ho_ten = input()
    ngay_sinh = input()
    diem1_str = input()
    diem2_str = input()
    diem3_str = input()

    thi_sinh = ThiSinh(ho_ten, ngay_sinh, diem1_str, diem2_str, diem3_str)

    print(thi_sinh)

if __name__ == "__main__":
    main()
class ComplexNumber:
    """
    Lớp mô tả một số phức với phần thực và phần ảo.
    """

    def __init__(self, real, imag):
        """
        Khởi tạo số phức với phần thực (real) và phần ảo (imag).
        """
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """
        Nạp chồng toán tử cộng (+).
        Thực hiện phép cộng hai số phức.
        """
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

    def __mul__(self, other):
        """
        Nạp chồng toán tử nhân (*).
        Thực hiện phép nhân hai số phức.
        """
        new_real = self.real * other.real - self.imag * other.imag
        new_imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(new_real, new_imag)

    def __str__(self):
        """
        Định dạng chuỗi biểu diễn số phức.
        Ví dụ: "a + bi" hoặc "a - bi".
        """
        # Nếu phần ảo là 0
        # if self.imag == 0:
        #     return f"{self.real}"
        # Nếu phần ảo dương
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        # Nếu phần ảo âm
        else:
            return f"{self.real} - {abs(self.imag)}i"

def solve():
    """
    Hàm chính để đọc đầu vào và xử lý các bộ test.
    """
    t = int(input())
    for _ in range(t):
        # Đọc a, b, c, d
        a, b, c, d = map(int, input().split())

        # Tạo hai số phức A và B
        A = ComplexNumber(a, b)
        B = ComplexNumber(c, d)

        # Tính T = A + B
        T = A + B

        # Tính C = (A + B) * A = T * A
        C = T * A

        # Tính D = (A + B)^2 = T * T
        D = T * T

        # In kết quả theo định dạng
        print(f"{C}, {D}")

# Chạy hàm giải
solve()
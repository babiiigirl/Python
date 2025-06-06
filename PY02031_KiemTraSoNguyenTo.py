import math

def is_prime(n):
    """
    Hàm kiểm tra xem một số nguyên dương n có phải là số nguyên tố không.
    Trả về True nếu n là số nguyên tố, ngược lại trả về False.
    """
    # Số nguyên tố phải lớn hơn 1
    if n <= 1:
        return False
    # 2 là số nguyên tố duy nhất chẵn
    if n == 2:
        return True
    # Bỏ qua các số chẵn khác 2
    if n % 2 == 0:
        return False
    # Chỉ cần kiểm tra các ước số lẻ từ 3 đến căn bậc hai của n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    # Nếu không tìm thấy ước nào, nó là số nguyên tố
    return True

def solve_prime_matrix():
    """
    Hàm chính đọc input, xử lý ma trận và in ra output
    (Phiên bản không xử lý ngoại lệ).
    """
    # Đọc kích thước N và M từ dòng đầu tiên
    n, m = map(int, input().split())

    # Duyệt qua N dòng tiếp theo để đọc ma trận
    for _ in range(n):
        # Đọc một hàng, tách các số và chuyển thành list số nguyên
        row = list(map(int, input().split()))
        
        # Tạo một list mới chứa kết quả (0 hoặc 1)
        output_row = [1 if is_prime(number) else 0 for number in row]
        
        # In hàng kết quả ra màn hình.
        print(*output_row)

# Gọi hàm chính để bắt đầu chương trình
solve_prime_matrix()
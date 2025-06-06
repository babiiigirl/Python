from itertools import combinations

def giai_bai_toan():
    """
    Đọc dữ liệu đầu vào từ bàn phím và in ra tất cả các tổ hợp chập K 
    của các phần tử khác nhau trong mảng theo thứ tự từ điển.
    """
    # Đọc N và K từ dòng đầu tiên
    n, k = map(int, input().split())

    # Đọc mảng A từ dòng thứ hai
    a = list(map(int, input().split()))

    # Lấy các phần tử khác nhau và sắp xếp chúng
    cac_phan_tu_khac_nhau = sorted(list(set(a)))

    # Tạo tất cả các tổ hợp chập K
    cac_to_hop = combinations(cac_phan_tu_khac_nhau, k)

    # In ra từng tổ hợp
    for to_hop in cac_to_hop:
        print(*to_hop) # Toán tử * dùng để giải nén tuple

# Gọi hàm giải bài toán
giai_bai_toan()
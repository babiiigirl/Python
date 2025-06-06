from itertools import permutations

def giai_bai_toan_hoan_vi():
    """
    Đọc một chuỗi ký tự đã sắp xếp và in ra tất cả các hoán vị 
    của nó theo thứ tự từ điển.
    """
    # Đọc chuỗi S từ bàn phím
    s = input().strip() # .strip() để loại bỏ khoảng trắng thừa nếu có

    # Tạo tất cả các hoán vị của chuỗi S
    # Vì S đã được sắp xếp, itertools.permutations sẽ trả về 
    # các hoán vị theo thứ tự từ điển.
    cac_hoan_vi = permutations(s)

    # In ra từng hoán vị
    for hoan_vi in cac_hoan_vi:
        # hoan_vi là một tuple ('X', 'Y', 'Z')
        # ''.join(hoan_vi) sẽ nối các ký tự lại thành chuỗi "XYZ"
        print(''.join(hoan_vi))

# Gọi hàm giải bài toán
giai_bai_toan_hoan_vi()
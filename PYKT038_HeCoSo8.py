def chuyen_doi_nhi_phan_sang_bat_phan():
    """
    Đọc một số nhị phân từ bàn phím và chuyển đổi nó sang hệ cơ số 8.
    """
    # Đọc chuỗi nhị phân từ input
    chuoi_nhi_phan = input().strip()

    # --- Cách 1: Sử dụng hàm có sẵn của Python (Đơn giản và hiệu quả) ---
    
    # Chuyển chuỗi nhị phân thành số nguyên (hệ 10)
    so_thap_phan = int(chuoi_nhi_phan, 2)
    
    # Chuyển số nguyên thành chuỗi bát phân (hệ 8)
    # Hàm oct() sẽ trả về chuỗi có dạng "0o..." (ví dụ: "0o314")
    chuoi_bat_phan = oct(so_thap_phan)
    
    # Loại bỏ tiền tố "0o" và in kết quả
    print(chuoi_bat_phan[2:])

# Gọi hàm để thực thi
chuyen_doi_nhi_phan_sang_bat_phan()
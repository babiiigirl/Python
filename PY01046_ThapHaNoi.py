def thap_ha_noi(so_dia, cot_nguon, cot_dich, cot_trung_gian):
    if so_dia == 0:
        return
    
    # Bước 1: Di chuyển (n-1) đĩa từ nguồn sang trung gian, dùng đích làm phụ trợ
    thap_ha_noi(so_dia - 1, cot_nguon, cot_trung_gian, cot_dich)
    
    # Bước 2: Di chuyển đĩa thứ n (đĩa lớn nhất ở bước này) từ nguồn sang đích
    #         Đây là lúc in ra bước di chuyển theo yêu cầu.
    print(f"{cot_nguon} -> {cot_dich}")
    
    # Bước 3: Di chuyển (n-1) đĩa từ trung gian sang đích, dùng nguồn làm phụ trợ
    thap_ha_noi(so_dia - 1, cot_trung_gian, cot_dich, cot_nguon)

N = int(input())
thap_ha_noi(N, 'A', 'C', 'B')
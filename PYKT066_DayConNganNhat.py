import math

# Hàm tính GCD của một dãy con liên tiếp
def solve_test_case(N, K, A):
    min_length = float('inf')  # Khởi tạo độ dài dãy con nhỏ nhất là vô hạn
    
    # Duyệt qua tất cả các phần tử trong mảng A[]
    for start in range(N):
        current_gcd = A[start]  # Khởi tạo GCD bắt đầu từ phần tử đầu tiên của dãy con
        if current_gcd % K != 0:
            continue  # Nếu phần tử đầu tiên không chia hết cho K, bỏ qua
        
        # Duyệt qua các phần tử tiếp theo
        for end in range(start, N):
            current_gcd = math.gcd(current_gcd, A[end])  # Cập nhật GCD dãy con
            if current_gcd == K:  # Nếu GCD của dãy con bằng K, kiểm tra độ dài
                min_length = min(min_length, end - start + 1)
            elif current_gcd < K:  # Nếu GCD nhỏ hơn K, không thể tìm thấy dãy con hợp lệ
                break

    return min_length if min_length != float('inf') else -1

# Hàm chính để xử lý nhiều test case
def main():
    T = int(input())  # Đọc số lượng bộ test
    for _ in range(T):
        N, K = map(int, input().split())  # Đọc N và K
        A = list(map(int, input().split()))  # Đọc mảng A[]
        
        # Giải quyết bài toán cho từng test case
        result = solve_test_case(N, K, A)
        print(result)

if __name__ == "__main__":
    main()

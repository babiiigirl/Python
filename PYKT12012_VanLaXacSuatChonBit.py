import sys

def sum_ones_up_to(n):
  """
  Tính tổng số bit 1 của tất cả các số từ 0 đến n.

  Args:
    n (int): Số nguyên giới hạn.

  Returns:
    int: Tổng số bit 1.
  """
  if n < 0:
      return 0
  
  # Chúng ta tính cho các số từ 0 đến n, nên có n+1 số
  n += 1 
  count = 0
  # Duyệt qua từng vị trí bit (k=0 là bit 2^0, k=1 là bit 2^1, ...)
  k = 0
  while (1 << k) <= n:
      # Lũy thừa của 2 tại vị trí k và k+1
      power_of_2_k = 1 << k
      power_of_2_k_plus_1 = 1 << (k + 1)
      
      # Tính số chu kỳ đầy đủ (mỗi chu kỳ có độ dài 2^(k+1))
      full_cycles = n // power_of_2_k_plus_1
      # Mỗi chu kỳ đầy đủ có 2^k số có bit 1 tại vị trí k
      count += full_cycles * power_of_2_k
      
      # Tính số bit 1 trong phần còn lại (chu kỳ chưa đầy đủ)
      remainder = n % power_of_2_k_plus_1
      # Phần còn lại sẽ có bit 1 nếu nó lớn hơn 2^k
      count += max(0, remainder - power_of_2_k)
      
      k += 1
  return count

def solve():
  """
  Giải quyết một bộ test: đọc A, B và tính xác suất.
  """
  try:
      # Đọc A và B từ input
      line = sys.stdin.readline()
      if not line: return False # Kết thúc file
      A, B = map(int, line.strip().split())
  except Exception as e:
      print(f"Lỗi đọc input: {e}")
      return False

  # Tính độ dài bit của A và B
  L_A = A.bit_length()
  L_B = B.bit_length()
  
  total_prob_sum = 0.0

  # Duyệt qua tất cả các độ dài bit có thể có trong đoạn [A, B]
  for L in range(L_A, L_B + 1):
      # Xác định đoạn con [start_range, end_range] trong [A, B]
      # mà tất cả các số đều có độ dài bit là L.
      start_range = max(A, 1 << (L - 1))
      end_range = min(B, (1 << L) - 1)

      # Nếu đoạn con không hợp lệ (ví dụ: A > B), bỏ qua
      if start_range > end_range:
          continue

      # Tính tổng số bit 1 trong đoạn con này
      sum_ones = sum_ones_up_to(end_range) - sum_ones_up_to(start_range - 1)
      
      # Cộng vào tổng xác suất (số bit 1 / độ dài bit)
      total_prob_sum += sum_ones / L

  # Tính xác suất trung bình bằng cách chia cho tổng số số trong đoạn [A, B]
  result = total_prob_sum / (B - A + 1)
  
  # In kết quả với 5 chữ số sau dấu phảy
  print(f"{result:.5f}")
  return True

def main():
  """
  Hàm chính để đọc số lượng bộ test và gọi hàm giải quyết cho mỗi bộ.
  """
  try:
      T_str = sys.stdin.readline()
      if not T_str: return
      T = int(T_str.strip())
  except Exception as e:
      print(f"Lỗi đọc số lượng test: {e}")
      return
      
  for _ in range(T):
      if not solve():
          break

# Chạy chương trình
if __name__ == "__main__":
    main()
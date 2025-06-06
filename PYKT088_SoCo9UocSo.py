import math
import bisect

def sieve(n):
    """Sàng Eratosthenes để tìm các số nguyên tố <= n."""
    primes = [True] * (n + 1)
    if n >= 0:
        primes[0] = False
    if n >= 1:
        primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, n + 1, i):
                primes[multiple] = False
    prime_numbers = [i for i, is_p in enumerate(primes) if is_p]
    return prime_numbers

def count_case1(N):
    """Đếm số có dạng p^8 <= N."""
    count = 0
    small_primes = [2, 3, 5, 7, 11, 13] 
    for p in small_primes:
        try:
            val = p ** 8
            if val <= N:
                count += 1
            else:
                break # Vì các số nguyên tố đã sắp xếp
        except OverflowError:
            break
    return count

def count_case2(N):
    """Đếm số có dạng p1^2 * p2^2 <= N."""
    M = int(N**0.5)
    
    # Nếu M quá nhỏ, không thể có p1 * p2 (nhỏ nhất là 2*3=6)
    if M < 6:
        return 0
        
    primes_list = sieve(M)
    count = 0
    num_primes = len(primes_list)
    
    for i in range(num_primes):
        p1 = primes_list[i]
        
        # Nếu p1 * p1 > M, thì p1 * p2 (với p2 > p1) chắc chắn > M
        if p1 * p1 > M :
             break

        # Giới hạn cho p2
        limit = M // p1
        
        # Tìm vị trí của số nguyên tố cuối cùng <= limit
        # bisect_right tìm vị trí chèn để duy trì thứ tự.
        # k là chỉ số của số nguyên tố ĐẦU TIÊN > limit.
        k = bisect.bisect_right(primes_list, limit)
        
        # Chúng ta cần đếm các số nguyên tố có chỉ số j sao cho i < j < k.
        # Số lượng là k - (i + 1). Đảm bảo không âm.
        count += max(0, k - i - 1)
        
    return count

def solve():
    """Đọc input và gọi các hàm tính toán."""
    try:
        N_str = input().strip()
        if not N_str:
            return
        N = int(N_str)
        
        c1 = count_case1(N)
        c2 = count_case2(N)
        
        print(c1 + c2)
    except Exception as e:
        print(f"Lỗi: {e}")

# Chạy hàm giải
solve()
def check(s1, s2):
    if '?' not in s1:
        return s1 == s2
    if len(s1) != len(s2):
        return False
    for p, v in zip(s1, s2): #nhận vào hai hay nhiều chuỗi (hoặc danh sách), rồi "ghép" các phần tử ở cùng vị trí lại với nhau thành từng cặp.
        # s1 = "?0"
        # s2 = "40"
        # zip("?0", "40") sẽ tạo ra các cặp: ('?', '4') và ('0', '0')
        if p != '?' and p != v:
            return False
    return True

def solve(s):
    a1, o, b1, _, c1 = s
    for a2 in range(10, 100):
        for b2 in range(10, 100):
            c2 = a2 + b2
            if 10 <= c2 <= 99:
                if check(o, '+') and check(a1, str(a2)) and check(b1, str(b2)) and check(c1, str(c2)):
                    print(f'{a2} + {b2} = {c2}')
                    return
                
            c2 = a2 - b2
            if 10 <= c2 <= 99:
                if check(o, '-') and check(a1, str(a2)) and check(b1, str(b2)) and check(c1, str(c2)):
                    print(f'{a2} - {b2} = {c2}')
                    return
            
            c2 = a2 * b2
            if 10 <= c2 <= 99:
                if check(o, '*') and check(a1, str(a2)) and check(b1, str(b2)) and check(c1, str(c2)):
                    print(f'{a2} * {b2} = {c2}')
                    return
               
            if a2 % b2 == 0: 
                c2 = a2 // b2
                if 10 <= c2 <= 99:
                    if check(o, '/') and check(a1, str(a2)) and check(b1, str(b2)) and check(c1, str(c2)):
                        print(f'{a2} / {b2} = {c2}')
                        return
    print("WRONG PROBLEM!")

t = int(input())
for _ in range(t):
    s = input().split()
    solve(s)
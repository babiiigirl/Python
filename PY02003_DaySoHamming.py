h = [1]
def hamminglist():
    i2 = i3 = i5 = 0
    while True:
        next2 = h[i2] * 2
        next3 = h[i3] * 3
        next5 = h[i5] * 5
        
        next_hamming = min(next2, next3, next5)
        if next_hamming > 10 ** 18:
            break
        h.append(next_hamming)
        if next_hamming == next2:
            i2 += 1
        if next_hamming == next3:
            i3 += 1
        if next_hamming == next5:
            i5 += 1

if __name__ == '__main__':
    t = int(input())
    hamminglist()
    hamming_map = {}
    for i, val in enumerate(h):
            hamming_map[val] = i + 1
    for _ in range(t):
        n = int(input())        
        if n in hamming_map:
            print(hamming_map[n])
        else:
            print('Not in sequence')
    
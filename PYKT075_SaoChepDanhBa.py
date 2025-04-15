with open('SOTAY.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]
i = 0
danhba = []
while i < len(lines):
    if lines[i].startswith('Ngay'):
        ngay = lines[i].split()[1]
        i += 1
    else:
        ten = lines[i]
        sdt = lines[i + 1]
        danhba.append((ten, sdt, ngay))
        i += 2
danhba.sort(key = lambda x: (x[0].split()[-1], x[0].split()[1]))
with open('DIENTHOAI.txt', 'w') as f:
    for ten, sdt, ngay in danhba:
        f.write(ten + ': ' + sdt + ' ' + ngay + '\n')
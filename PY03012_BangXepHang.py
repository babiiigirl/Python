class SinhVien:
    def __init__(self, name, ac, submit):
        self.name = name
        self.ac = ac
        self.submit = submit
    def __str__(self):
        return self.name + " " + str(self.ac) + " " + str(self.submit)

n = int(input())
a = []
for _ in range(n):
    name = input()
    c, t = map(int, input().split())
    a.append(SinhVien(name, c, t))
a.sort(key = lambda x : (-x.ac, x.submit, x.name))
for i in a:
    print(i)
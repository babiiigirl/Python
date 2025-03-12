t = int(input())
for _ in range(t):
    s = input()
    t = ""
    for char in s:
        if char.isalpha():
            t += " "
        else:
            t += char
    a = list(map(int, t.split()))
    print(min(a))
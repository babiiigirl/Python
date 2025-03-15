import sys

a = sys.stdin.read().split()
s = set(int(x) % 42 for x in a)
print(len(s))
t = int(input())
dict = {}
topic = None
for _ in range(t):
    s = input().strip()
    if not s: 
        topic = None
    elif topic == None:
        topic = s
        dict[topic] = 0
    else: dict[topic] += 1
for x in dict:
    print(x + ': ' + str(dict[x]))
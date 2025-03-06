import random

alien_color = ['green', 'yellow', 'red']
i = random.choice(alien_color)
print(i)
if i == 'green':
    print("ban duoc cong 5 diem")
elif i == 'yellow':
    print("ban duoc cong 10 diem")
else:
    print("ban duoc cong 15 diem")
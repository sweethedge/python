list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))

list(map(lambda x: x * 3, [1,2,3,4]))

list1 = [-8, 2, 7, 5, -3, 5, 0, 1]
max(list1) + min(list1)

round((17 / 3), 4)

import random

a = []
for _ in range(0, 7):
    b = random.randint(0, 46)
    a.append(b)

print(a)

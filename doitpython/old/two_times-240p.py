import random
import numpy as np


def two_times(x): return x * 2


# list(map(two_times, [1, 2, 3, 4]))
list(map(lambda x: x * 2, [1, 2, 3, 4]))

result = []

while len(result) < 6:
    a = random.randint(1, 45)
    if a not in result:
        result.append(a)

print(result)



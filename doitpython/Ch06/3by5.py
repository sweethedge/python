result = []
for n in range(1000):
    if n % 3 or n % 5 == 0:
        result.append(n)

print(result)